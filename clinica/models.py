"""
Bloque de comentarios:
Modelos principales para Salud Vital Ltda.
Incluye mejoras requeridas: CHOICES (género y estado) y nuevas tablas (Aseguradora, Sala).
Relaciones ManyToOne/ManyToMany según el dominio.
"""
from django.db import models

class Aseguradora(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Sala(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    piso = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"Sala {self.numero} (Piso {self.piso})"

class Medico(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=120)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name="medicos")
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True, related_name="medicos")
    def __str__(self):
        return f"{self.nombre} - {self.especialidad.nombre}"

class Paciente(models.Model):
    GENERO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro/Prefiero no decir"),
    ]
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default="O")
    aseguradora = models.ForeignKey(Aseguradora, on_delete=models.SET_NULL, null=True, blank=True, related_name="pacientes")
    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    medicamentos = models.ManyToManyField(Medicamento, related_name="tratamientos", blank=True)
    def __str__(self):
        return self.nombre

class ConsultaMedica(models.Model):
    ESTADO_CHOICES = [
        ("PEND", "Pendiente"),
        ("REAL", "Realizada"),
        ("CANC", "Cancelada"),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name="consultas")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name="consultas")
    fecha = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=4, choices=ESTADO_CHOICES, default="PEND")
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.SET_NULL, null=True, blank=True, related_name="consultas")
    def __str__(self):
        return f"Consulta {self.id} - {self.paciente} con {self.medico} ({self.fecha.date()})"

class RecetaMedica(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE, related_name="recetas")
    indicaciones = models.TextField()
    fecha_emision = models.DateField(auto_now_add=True)
    medicamentos = models.ManyToManyField(Medicamento, related_name="recetas", blank=True)
    def __str__(self):
        return f"Receta {self.id} (Consulta {self.consulta_id})"
