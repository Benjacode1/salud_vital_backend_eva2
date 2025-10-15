"""
Bloque de comentarios:
ViewSets de DRF para CRUD por entidad. Agrega filtros donde corresponde.
"""
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica, Aseguradora, Sala
from .serializers import (
    EspecialidadSerializer, PacienteSerializer, MedicoSerializer,
    ConsultaMedicaSerializer, TratamientoSerializer, MedicamentoSerializer,
    RecetaMedicaSerializer, AseguradoraSerializer, SalaSerializer
)
from .filters import MedicoFilter, PacienteFilter, ConsultaFilter

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer


class AseguradoraViewSet(viewsets.ModelViewSet):
    queryset = Aseguradora.objects.all()
    serializer_class = AseguradoraSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.select_related("aseguradora").all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PacienteFilter

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.prefetch_related("medicamentos").all()
    serializer_class = TratamientoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.select_related("especialidad", "sala").all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MedicoFilter

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.select_related("paciente", "medico", "especialidad", "tratamiento").all()
    serializer_class = ConsultaMedicaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConsultaFilter

class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.select_related("consulta").prefetch_related("medicamentos").all()
    serializer_class = RecetaMedicaSerializer
