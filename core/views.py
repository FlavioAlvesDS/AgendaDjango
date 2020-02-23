from django.shortcuts import render, redirect
from core.models import Evento

# Criando uma função para mostrar a lista de eventos e depois chamar no html utilizando o for
def lista_eventos(request):

    evento = Evento.objects.all() #objects.all() para mostrar todos os eventos "poderia filtrar utilizando objects.get(e o paramentro aqui)"
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)

#função para redirecionar o navegador para abrir na pagina agenda
#def index(request):
 #   return redirect('/agenda')