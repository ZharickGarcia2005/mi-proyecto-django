from .models import Persona

def datos_persona(request):
    # Toma el registro de la base de datos
    persona = Persona.objects.first()
    return {'persona': persona}
