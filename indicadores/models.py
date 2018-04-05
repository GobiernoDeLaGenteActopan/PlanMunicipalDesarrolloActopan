from django.db import models

class Indicadores(models.Model):
    indicador = models.CharField(max_length=200)
    eje = models.CharField(max_length=250)
    objetivo = models.TextField()
    estrategia = models.TextField()
    linea_accion = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    nombre_formato = models.CharField(max_length=140, blank=True, null=True)
    dimension_medir = models.CharField(max_length=140)
    observaciones = models.TextField(blank=True, null=True)
    metodo_calculo = models.CharField(max_length=140, blank=True, null=True)
    frecuencia_medicion = models.CharField(max_length=50, blank=True, null=True)
    fuente=models.CharField(max_length=50, blank=True, null=True)
    responsable=models.CharField(max_length=140)
    meta_programada=models.CharField(max_length=50, blank=True, null=True)
    sentido_indicador=models.CharField(max_length=50, default="Ascendente")
    medicion_anterior=models.CharField(max_length=50, blank=True, null=True)
    linea_base=models.CharField(max_length=50, blank=True, null=True)
    date=models.DateTimeField(auto_now=True)
    elaboro=models.CharField(max_length=140)

    def __str__(self):
        return self.indicador
