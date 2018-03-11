
from django.db import models
from django.utils import timezone

class Post(models.Model):
    Autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=200)
    Texto = models.TextField()
    Creado_Fecha = models.DateTimeField(default=timezone.now)
    Publicado = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.Publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.Titulo
