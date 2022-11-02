from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    cor = models.CharField(max_length=7)

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.URLField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.titulo
