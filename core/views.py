from datetime import datetime,timedelta




from django.core.checks import messages
from django.http.response import Http404,JsonResponse
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout




#caso nao esteja usuario logado redireciona para a pagina login

def login_user(requeste):
   return render(requeste,'login.html')



def logout_user(request):
    logout(request)
    return redirect('/')



#função para vautenticar usuario
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:

            return redirect('/')



# Criando uma função para mostrar a lista de eventos e depois chamar no html utilizando o for
@login_required(login_url='/login/')
def lista_eventos(request, ):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=12)
    evento = Evento.objects.filter(usuario=usuario,# mostrada a lista de eventos daquele usuario logado
                                  data_evento__gt=data_atual)
    #evento = Evento.objects.all() #objects.all() para mostrar todos os eventos "poderia filtrar utilizando objects.get(e o paramentro aqui)"
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)



@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render (request,'evento.html',dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        local = request.POST.get('local')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento :
            # a linh abaixo cofere se tem usuario logado
            evento = Evento.objects.get(id=id_evento)
            #a linha abaixo faz um update na tbela somente se o usurio for o mesmo do usuario do evento
            if evento.usuario==usuario:
                evento.titulo=titulo
                evento.local=local
                evento.descricao=descricao
                evento.data_evento=data_evento
                evento.save()
            #a linha a baixo faz um update na tabela utilizando o id
            #----->OUTRA MANEIRA DE FAZER O UPDATE <-------
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,data_evento=data_evento,local=local,descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario,
                                  local=local
                                  )
    return redirect('/')



@login_required(login_url='/login/')
#função para deletar um evento aceita excluir apenas eventos de quem esta logado
def delete_evento(request,id_evento):
    usuario = request.user
    try:
        evento =  Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
       evento.delete()
    else:
        raise Http404()
    return redirect('/')


#a funçaõ abaixo retorna uma lista json
@login_required(login_url='/login/')
def json_lista(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id','titulo')#retornara uma lista do tipo json
    return JsonResponse(list(evento),safe=False)


#outra maneira de redirecionar a pagina
#{
    # função para redirecionar o navegador para abrir na pagina agenda
    # def index(request):
    # return redirect('/agenda')
# }

