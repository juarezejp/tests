from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    clasificacion = models.CharField(max_length=50)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Horario(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.hora_inicio.strftime('%Y-%m-%d %H:%M')}"


class Asiento(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    numero_asiento = models.CharField(max_length=10)#, unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Asiento {self.numero_asiento} ({'Disponible' if self.disponible else 'No Disponible'}) para {self.pelicula.titulo}"
