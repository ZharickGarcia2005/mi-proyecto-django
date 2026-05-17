from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    # Esto evita que se creen múltiples personas por error en el panel
    def has_add_permission(self, request):
        if Persona.objects.exists():
            return False
        return True
    