from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.


# COMANDO PARA CRIAR UMA TABELA NO BANCO
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    local = models.CharField(blank=True,max_length=100,null=True)
    descricao = models.TextField(blank=True,null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_craica = models.DateTimeField(auto_now=True,verbose_name='Data de Criacão')
    #esse comando adciona o campo usuario a tabela como uma chave estrangeira
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    # apos isso digite no seu terminal os comandos
    # python makemigrations <core> o nome do seu app, vai ser gerado um arquivo
    # python sqlmigrate core <aqui vai o nome do arquivo criado>

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

    #mudando o formato da hora para padrao que o navegador entende para preeencher o form na hora do update
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento<datetime.now():
            return True
        else:
            return False

