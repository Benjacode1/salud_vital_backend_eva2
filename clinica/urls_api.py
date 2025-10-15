from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import (
    EspecialidadViewSet, PacienteViewSet, MedicoViewSet, ConsultaMedicaViewSet,
    TratamientoViewSet, MedicamentoViewSet, RecetaMedicaViewSet,
    AseguradoraViewSet, SalaViewSet
)

router = DefaultRouter()
router.register(r"especialidades", EspecialidadViewSet)
router.register(r"pacientes", PacienteViewSet)
router.register(r"medicos", MedicoViewSet)
router.register(r"consultas", ConsultaMedicaViewSet)
router.register(r"tratamientos", TratamientoViewSet)
router.register(r"medicamentos", MedicamentoViewSet)
router.register(r"recetas", RecetaMedicaViewSet)
router.register(r"aseguradoras", AseguradoraViewSet)
router.register(r"salas", SalaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
