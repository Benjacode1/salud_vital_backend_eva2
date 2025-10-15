"""
Bloque de comentarios:
Vistas genéricas (class-based) para CRUD HTML fuera del admin.
Incluyen ListView, CreateView, UpdateView y DeleteView.
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica

class BaseSuccessMixin:
    success_url = reverse_lazy("web:home")

class HomeView(ListView):
    template_name = "clinica/home.html"
    model = Especialidad
    context_object_name = "especialidades"

# Especialidad
class EspecialidadList(ListView):
    model = Especialidad
    template_name = "clinica/especialidad_list.html"

class EspecialidadCreate(CreateView):
    model = Especialidad
    fields = ["nombre", "descripcion"]
    template_name = "clinica/especialidad_form.html"
    success_url = reverse_lazy("web:especialidad_list")

class EspecialidadUpdate(UpdateView):
    model = Especialidad
    fields = ["nombre", "descripcion"]
    template_name = "clinica/especialidad_form.html"
    success_url = reverse_lazy("web:especialidad_list")

class EspecialidadDelete(DeleteView):
    model = Especialidad
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:especialidad_list")

# Paciente
class PacienteList(ListView):
    model = Paciente
    template_name = "clinica/paciente_list.html"

class PacienteCreate(CreateView):
    model = Paciente
    fields = ["rut", "nombre", "fecha_nacimiento", "genero", "aseguradora"]
    template_name = "clinica/paciente_form.html"
    success_url = reverse_lazy("web:paciente_list")

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ["rut", "nombre", "fecha_nacimiento", "genero", "aseguradora"]
    template_name = "clinica/paciente_form.html"
    success_url = reverse_lazy("web:paciente_list")

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:paciente_list")

# Medico
class MedicoList(ListView):
    model = Medico
    template_name = "clinica/medico_list.html"

class MedicoCreate(CreateView):
    model = Medico
    fields = ["rut", "nombre", "especialidad", "sala"]
    template_name = "clinica/medico_form.html"
    success_url = reverse_lazy("web:medico_list")

class MedicoUpdate(UpdateView):
    model = Medico
    fields = ["rut", "nombre", "especialidad", "sala"]
    template_name = "clinica/medico_form.html"
    success_url = reverse_lazy("web:medico_list")

class MedicoDelete(DeleteView):
    model = Medico
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:medico_list")

# Consulta
class ConsultaList(ListView):
    model = ConsultaMedica
    template_name = "clinica/consulta_list.html"

class ConsultaCreate(CreateView):
    model = ConsultaMedica
    fields = ["paciente", "medico", "especialidad", "fecha", "motivo", "estado", "tratamiento"]
    template_name = "clinica/consulta_form.html"
    success_url = reverse_lazy("web:consulta_list")

class ConsultaUpdate(UpdateView):
    model = ConsultaMedica
    fields = ["paciente", "medico", "especialidad", "fecha", "motivo", "estado", "tratamiento"]
    template_name = "clinica/consulta_form.html"
    success_url = reverse_lazy("web:consulta_list")

class ConsultaDelete(DeleteView):
    model = ConsultaMedica
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:consulta_list")

# Tratamiento
class TratamientoList(ListView):
    model = Tratamiento
    template_name = "clinica/tratamiento_list.html"

class TratamientoCreate(CreateView):
    model = Tratamiento
    fields = ["nombre", "descripcion", "medicamentos"]
    template_name = "clinica/tratamiento_form.html"
    success_url = reverse_lazy("web:tratamiento_list")

class TratamientoUpdate(UpdateView):
    model = Tratamiento
    fields = ["nombre", "descripcion", "medicamentos"]
    template_name = "clinica/tratamiento_form.html"
    success_url = reverse_lazy("web:tratamiento_list")

class TratamientoDelete(DeleteView):
    model = Tratamiento
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:tratamiento_list")

# Medicamento
class MedicamentoList(ListView):
    model = Medicamento
    template_name = "clinica/medicamento_list.html"

class MedicamentoCreate(CreateView):
    model = Medicamento
    fields = ["nombre", "descripcion"]
    template_name = "clinica/medicamento_form.html"
    success_url = reverse_lazy("web:medicamento_list")

class MedicamentoUpdate(UpdateView):
    model = Medicamento
    fields = ["nombre", "descripcion"]
    template_name = "clinica/medicamento_form.html"
    success_url = reverse_lazy("web:medicamento_list")

class MedicamentoDelete(DeleteView):
    model = Medicamento
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:medicamento_list")

# Receta
class RecetaList(ListView):
    model = RecetaMedica
    template_name = "clinica/receta_list.html"

class RecetaCreate(CreateView):
    model = RecetaMedica
    fields = ["consulta", "indicaciones", "medicamentos"]
    template_name = "clinica/receta_form.html"
    success_url = reverse_lazy("web:receta_list")

class RecetaUpdate(UpdateView):
    model = RecetaMedica
    fields = ["consulta", "indicaciones", "medicamentos"]
    template_name = "clinica/receta_form.html"
    success_url = reverse_lazy("web:receta_list")

class RecetaDelete(DeleteView):
    model = RecetaMedica
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:receta_list")
