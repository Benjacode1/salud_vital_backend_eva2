from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica

class HomeView(ListView):
    template_name = "clinica/home.html"
    model = Especialidad
    context_object_name = "especialidades"

# ------- Helpers -------
def delete_success(self, request, obj_name, url_name):
    messages.success(request, f"{obj_name} eliminado correctamente.")
    return super(self.__class__, self).delete(request, *self.args, **self.kwargs)

# ------- Especialidad -------
class EspecialidadList(ListView):
    model = Especialidad
    template_name = "clinica/especialidad_list.html"

class EspecialidadCreate(SuccessMessageMixin, CreateView):
    model = Especialidad
    fields = ["nombre", "descripcion"]
    template_name = "clinica/especialidad_form.html"
    success_url = reverse_lazy("web:especialidad_list")
    success_message = "Especialidad creada correctamente."

class EspecialidadUpdate(SuccessMessageMixin, UpdateView):
    model = Especialidad
    fields = ["nombre", "descripcion"]
    template_name = "clinica/especialidad_form.html"
    success_url = reverse_lazy("web:especialidad_list")
    success_message = "Especialidad actualizada correctamente."

class EspecialidadDelete(DeleteView):
    model = Especialidad
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:especialidad_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Especialidad eliminada correctamente.")
        return super().delete(request, *args, **kwargs)

# ------- Paciente -------
class PacienteList(ListView):
    model = Paciente
    template_name = "clinica/paciente_list.html"

class PacienteCreate(SuccessMessageMixin, CreateView):
    model = Paciente
    fields = ["rut", "nombre", "fecha_nacimiento", "genero", "aseguradora"]
    template_name = "clinica/paciente_form.html"
    success_url = reverse_lazy("web:paciente_list")
    success_message = "Paciente creado correctamente."

class PacienteUpdate(SuccessMessageMixin, UpdateView):
    model = Paciente
    fields = ["rut", "nombre", "fecha_nacimiento", "genero", "aseguradora"]
    template_name = "clinica/paciente_form.html"
    success_url = reverse_lazy("web:paciente_list")
    success_message = "Paciente actualizado correctamente."

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:paciente_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Paciente eliminado correctamente.")
        return super().delete(request, *args, **kwargs)

# ------- Médico -------
class MedicoList(ListView):
    model = Medico
    template_name = "clinica/medico_list.html"

class MedicoCreate(SuccessMessageMixin, CreateView):
    model = Medico
    fields = ["rut", "nombre", "especialidad", "sala"]
    template_name = "clinica/medico_form.html"
    success_url = reverse_lazy("web:medico_list")
    success_message = "Médico creado correctamente."

class MedicoUpdate(SuccessMessageMixin, UpdateView):
    model = Medico
    fields = ["rut", "nombre", "especialidad", "sala"]
    template_name = "clinica/medico_form.html"
    success_url = reverse_lazy("web:medico_list")
    success_message = "Médico actualizado correctamente."

class MedicoDelete(DeleteView):
    model = Medico
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:medico_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Médico eliminado correctamente.")
        return super().delete(request, *args, **kwargs)

# ------- Consulta -------
class ConsultaList(ListView):
    model = ConsultaMedica
    template_name = "clinica/consulta_list.html"

class ConsultaCreate(SuccessMessageMixin, CreateView):
    model = ConsultaMedica
    fields = ["paciente", "medico", "especialidad", "fecha", "motivo", "estado", "tratamiento"]
    template_name = "clinica/consulta_form.html"
    success_url = reverse_lazy("web:consulta_list")
    success_message = "Consulta creada correctamente."

class ConsultaUpdate(SuccessMessageMixin, UpdateView):
    model = ConsultaMedica
    fields = ["paciente", "medico", "especialidad", "fecha", "motivo", "estado", "tratamiento"]
    template_name = "clinica/consulta_form.html"
    success_url = reverse_lazy("web:consulta_list")
    success_message = "Consulta actualizada correctamente."

class ConsultaDelete(DeleteView):
    model = ConsultaMedica
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:consulta_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Consulta eliminada correctamente.")
        return super().delete(request, *args, **kwargs)

# ------- Tratamiento -------
class TratamientoList(ListView):
    model = Tratamiento
    template_name = "clinica/tratamiento_list.html"

class TratamientoCreate(SuccessMessageMixin, CreateView):
    model = Tratamiento
    fields = ["nombre", "descripcion", "medicamentos"]
    template_name = "clinica/tratamiento_form.html"
    success_url = reverse_lazy("web:tratamiento_list")
    success_message = "Tratamiento creado correctamente."

class TratamientoUpdate(SuccessMessageMixin, UpdateView):
    model = Tratamiento
    fields = ["nombre", "descripcion", "medicamentos"]
    template_name = "clinica/tratamiento_form.html"
    success_url = reverse_lazy("web:tratamiento_list")
    success_message = "Tratamiento actualizado correctamente."

class TratamientoDelete(DeleteView):
    model = Tratamiento
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:tratamiento_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Tratamiento eliminado correctamente.")
        return super().delete(request, *args, **kwargs)

# ------- Medicamento -------
class MedicamentoList(ListView):
    model = Medicamento
    template_name = "clinica/medicamento_list.html"

class MedicamentoCreate(SuccessMessageMixin, CreateView):
    model = Medicamento
    fields = ["nombre", "descripcion"]
    template_name = "clinica/medicamento_form.html"
    success_url = reverse_lazy("web:medicamento_list")
    success_message = "Medicamento creado correctamente."

class MedicamentoUpdate(SuccessMessageMixin, UpdateView):
    model = Medicamento
    fields = ["nombre", "descripcion"]
    template_name = "clinica/medicamento_form.html"
    success_url = reverse_lazy("web:medicamento_list")
    success_message = "Medicamento actualizado correctamente."

class MedicamentoDelete(DeleteView):
    model = Medicamento
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:medicamento_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Medicamento eliminado correctamente.")
        return super().delete(request, *args, **kwargs)

# ------- Receta -------
class RecetaList(ListView):
    model = RecetaMedica
    template_name = "clinica/receta_list.html"

class RecetaCreate(SuccessMessageMixin, CreateView):
    model = RecetaMedica
    fields = ["consulta", "indicaciones", "medicamentos"]
    template_name = "clinica/receta_form.html"
    success_url = reverse_lazy("web:receta_list")
    success_message = "Receta creada correctamente."

class RecetaUpdate(SuccessMessageMixin, UpdateView):
    model = RecetaMedica
    fields = ["consulta", "indicaciones", "medicamentos"]
    template_name = "clinica/receta_form.html"
    success_url = reverse_lazy("web:receta_list")
    success_message = "Receta actualizada correctamente."

class RecetaDelete(DeleteView):
    model = RecetaMedica
    template_name = "clinica/confirm_delete.html"
    success_url = reverse_lazy("web:receta_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Receta eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
