"""
Bloque de comentarios:
- Define rutas para admin, API (DRF con router), vistas HTML y documentación Swagger/Redoc.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Salud Vital",
        default_version="v1",
        description="Documentación de la API para la clínica Salud Vital Ltda.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("clinica.urls_api")),
    path("web/", include("clinica.urls_web")),
    re_path(r"^docs/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
