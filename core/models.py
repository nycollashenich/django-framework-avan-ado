from django.db import models

from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True) # na adição
    modificado = models.DateField('Atualização', auto_now=True) # na modificação
    ativo= models.BooleanField('Ativo?', default=True)

    class Meta():
        abstract = True

class Servico(Base):
    ICONE_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuário'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    }
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=100)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

        def __str__(self):
            return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta():
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
        
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

        def __str__(self):
            return self.nome

class Recurso(Base):
    ICONE_RECURSO_CHOICES = {
        ('lni-rocket','Foguete'),
        ('lni-laptop-phone','Computador'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf','Folha'),
        ('lni-layers','Camadas'),
    }
    recurso = models.CharField('Recurso', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_RECURSO_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

        def __str__(self):
            return self.recurso
        
class Preco(Base):
    ICONE_PRECO_CHOICES = {
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Agua'),
        ('lni-star', 'Estrela'),
    }
    preco = models.CharField('Preço', max_length=100)
    tipo_plano = models.CharField('Plano', max_length=100,) 
    descricao_users = models.CharField('Descrição users', max_length=100,)
    descricao_gb = models.CharField('Descrição gb', max_length=100,)
    descricao_suporte = models.CharField('Descrição sup', max_length=100,)
    descricao_updates = models.CharField('Descrição up', max_length=100,)
    botao = models.CharField('Botão', max_length=100)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_PRECO_CHOICES)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

        def __str__(self) -> str:
            return self.preco