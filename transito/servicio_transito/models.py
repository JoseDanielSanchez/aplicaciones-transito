from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class ReporteTransito(models.Model):

    ESTADO_TRANSITO = (
        ('carretera_despejada', 'Carretera despejada'),
        ('congestionamiento', 'Congestionamiento vehicular'),
        ('colision', 'Colisión'),
        ('reten', 'Retén policial'),
        ('obras', 'Obras viales'),
    )

    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True, blank=True)
    tipo = models.CharField(max_length=25, choices=ESTADO_TRANSITO )
    descripcion = models.CharField(max_length=1200, blank=True )
    latitud = models.DecimalField(max_digits=20, decimal_places=8, default=0.00)
    longitud = models.DecimalField(max_digits=20, decimal_places=8, default=0.00)
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)

