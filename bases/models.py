from django.db import models
class aprendiz(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, unique=True)
    tipo_de_documento = models.CharField(max_length=25)

    ficha = models.ForeignKey(
        'programa',
        on_delete=models.CASCADE,
        related_name='aprendices',
        null=True,
        blank=True,
    )

    competencias = models.ManyToManyField(
        'competencias',
        related_name='aprendices',
        blank=True,
    )

    def _str_(self):
        return f'{self.nombre} {self.apellido} - {self.documento} - {self.correo} - {self.telefono} - {self.tipo_de_documento}'


class programa(models.Model):
    nombre = models.CharField(max_length=30)
    ficha = models.IntegerField(unique=True)
    jornada = models.CharField(max_length=15)
    lugar = models.CharField(max_length=20)
    duracion = models.CharField(max_length=30)
    modalidad = models.CharField(max_length=15)
    nivel_de_profecion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.nombre} - Ficha {self.ficha} - {self.jornada} - {self.duracion} -{self.modalidad} - {self.nivel_de_profecion} - {self.descripcion}'


class instructor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    especialidad = models.CharField(max_length=25)
    documento = models.CharField(max_length=20, unique=True)

    
    

    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, unique=True)

    def _str_(self):
        return f'{self.nombre} {self.apellido} - {self.especialidad}'


class competencias(models.Model):
    nombre = models.CharField(max_length=30)

    instructor = models.ForeignKey(
        'instructor',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def _str_(self):
        return self.nombre