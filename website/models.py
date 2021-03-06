from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros'),
    )
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=50,
        verbose_name='Sobrenome'
    )
    data_nascimento = models.DateField(
        verbose_name = 'Data de Nascimento'
    )
    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True
    )
    str_cep = models.CharField(
        max_length=10,
        verbose_name='CEP'
    )
    str_numero = models.CharField(
        max_length=5,
        verbose_name='Número Res.'
    )
    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento'
    )
    genero = models.CharField(
        choices=GENEROS,
        max_length=255,
        verbose_name='Gênero'
    )

    telefone = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Telefone'
    ) 

    celular = models.CharField(
        max_length=255,
        verbose_name='Celular'
    ) 

    motivo = models.TextField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome + ' ' + self.sobrenome




class Ong(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome da ong'
    )
    responsavel = models.CharField(
        max_length=50,
        verbose_name='responsavel'
    )
    endereco = models.CharField(
        max_length=255,
        verbose_name ='endereco'
    )
    telefone = models.CharField(
        max_length=255,
        verbose_name='telefone'
    )
    horario = models.CharField(
        max_length=10,
        verbose_name='horario'
    )
    observacao = models.CharField(
        max_length=255,
        verbose_name='observacao'
    )

    observacao = models.TextField

    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome

class Pet(models.model):
    PORTE = (
        ('P', 'pequeno'),
        ('M', 'medio'),
        ('G', 'grande'),
    )
    nome = models.CharField(
        max_length=225,
        verbose_name = 'nome',
    )
        raca = models.CharField(
        max_length=225,
        verbose_name = 'raca',
    )
        porte = models.CharField(
        max_length=225,
        verbose_name = 'porte',
        choices=PORTE
    )
        peso = models.floatField(
        verbose_name = 'peso',
    )

    dono = models.ForeingKey(Pessoa,
        on_delete=None
    )
        criado_em = models.DateTimeField(
        auto_now_add=True
    )
    ativo = models.BooleanField(
        default=True
    )