from django.conf import settings

def footer_ctx(request):
    return {
        "FOOTER_NOMBRE": getattr(settings, "FOOTER_NOMBRE", ""),
        "FOOTER_SECCION": getattr(settings, "FOOTER_SECCION", ""),
        "FOOTER_ANO": getattr(settings, "FOOTER_ANO", ""),
    }
