from django.core.checks import messages
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
    evento = Evento.objects.filter(usuario=usuario) # mostrada a lista de eventos daquele usuario logado
    #evento = Evento.objects.all() #objects.all() para mostrar todos os eventos "poderia filtrar utilizando objects.get(e o paramentro aqui)"
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)

@login_required(login_url='/login/')
def evento(request):
    return render (request,'evento.html')
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')


#outra maneira de redirecionar a pagina
#{
    # função para redirecionar o navegador para abrir na pagina agenda
    # def index(request):
    # return redirect('/agenda')
# }

