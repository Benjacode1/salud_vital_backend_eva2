"""
Bloque de comentarios:
Filtros utilizando django-filter para búsquedas por campos clave.
- Médicos por especialidad
- Pacientes por aseguradora
- Consultas por médico, especialidad o paciente
"""
import django_filters
from .models import Medico, Paciente, ConsultaMedica

class MedicoFilter(django_filters.FilterSet):
    especialidad__nombre = django_filters.CharFilter(field_name="especialidad__nombre", lookup_expr="icontains")
    class Meta:
        model = Medico
        fields = ["especialidad"]

class PacienteFilter(django_filters.FilterSet):
    aseguradora__nombre = django_filters.CharFilter(field_name="aseguradora__nombre", lookup_expr="icontains")
    class Meta:
        model = Paciente
        fields = ["aseguradora"]

class ConsultaFilter(django_filters.FilterSet):
    medico = django_filters.NumberFilter(field_name="medico__id")
    especialidad = django_filters.NumberFilter(field_name="especialidad__id")
    paciente = django_filters.NumberFilter(field_name="paciente__id")
    class Meta:
        model = ConsultaMedica
        fields = ["medico", "especialidad", "paciente", "estado"]
