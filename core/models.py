from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# COMANDO PARA CRIAR UMA TABELA NO BANCO
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_craica = models.DateTimeField(auto_now=True,verbose_name='Data de Criacão')
    #esse comando adciona o campo usuario a tabela como uma chave estrangeira
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)


    # COMANDO PARA CRIAR A TABELA COM O NOME EVENTO, POIS O DJANGO GERA AUTOMATICO
    class Meta:
        db_table = 'evento'

    # comando para que o django chame o objeto com o nome certo
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        #define a data e hora em um padrao brasileiro
        #e chame a função no for no html
        return self.data_evento.strftime('%d/%m/%Y - %H:%M hrs')

    # apos isso digite no seu terminal os comandos
    # python makemigrations <core> o nome do seu app, vai ser gerado um arquivo
    # python sqlmigrate core <aqui vai o nome do arquivo criado>