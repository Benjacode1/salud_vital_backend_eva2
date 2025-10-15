from django.urls import path
from . import views_web as v

app_name = "web"

urlpatterns = [
    path("", v.HomeView.as_view(), name="home"),

    path("especialidad/", v.EspecialidadList.as_view(), name="especialidad_list"),
    path("especialidad/crear/", v.EspecialidadCreate.as_view(), name="especialidad_create"),
    path("especialidad/<int:pk>/editar/", v.EspecialidadUpdate.as_view(), name="especialidad_update"),
    path("especialidad/<int:pk>/eliminar/", v.EspecialidadDelete.as_view(), name="especialidad_delete"),

    path("paciente/", v.PacienteList.as_view(), name="paciente_list"),
    path("paciente/crear/", v.PacienteCreate.as_view(), name="paciente_create"),
    path("paciente/<int:pk>/editar/", v.PacienteUpdate.as_view(), name="paciente_update"),
    path("paciente/<int:pk>/eliminar/", v.PacienteDelete.as_view(), name="paciente_delete"),

    path("medico/", v.MedicoList.as_view(), name="medico_list"),
    path("medico/crear/", v.MedicoCreate.as_view(), name="medico_create"),
    path("medico/<int:pk>/editar/", v.MedicoUpdate.as_view(), name="medico_update"),
    path("medico/<int:pk>/eliminar/", v.MedicoDelete.as_view(), name="medico_delete"),

    path("consulta/", v.ConsultaList.as_view(), name="consulta_list"),
    path("consulta/crear/", v.ConsultaCreate.as_view(), name="consulta_create"),
    path("consulta/<int:pk>/editar/", v.ConsultaUpdate.as_view(), name="consulta_update"),
    path("consulta/<int:pk>/eliminar/", v.ConsultaDelete.as_view(), name="consulta_delete"),

    path("tratamiento/", v.TratamientoList.as_view(), name="tratamiento_list"),
    path("tratamiento/crear/", v.TratamientoCreate.as_view(), name="tratamiento_create"),
    path("tratamiento/<int:pk>/editar/", v.TratamientoUpdate.as_view(), name="tratamiento_update"),
    path("tratamiento/<int:pk>/eliminar/", v.TratamientoDelete.as_view(), name="tratamiento_delete"),

    path("medicamento/", v.MedicamentoList.as_view(), name="medicamento_list"),
    path("medicamento/crear/", v.MedicamentoCreate.as_view(), name="medicamento_create"),
    path("medicamento/<int:pk>/editar/", v.MedicamentoUpdate.as_view(), name="medicamento_update"),
    path("medicamento/<int:pk>/eliminar/", v.MedicamentoDelete.as_view(), name="medicamento_delete"),

    path("receta/", v.RecetaList.as_view(), name="receta_list"),
    path("receta/crear/", v.RecetaCreate.as_view(), name="receta_create"),
    path("receta/<int:pk>/editar/", v.RecetaUpdate.as_view(), name="receta_update"),
    path("receta/<int:pk>/eliminar/", v.RecetaDelete.as_view(), name="receta_delete"),
]
