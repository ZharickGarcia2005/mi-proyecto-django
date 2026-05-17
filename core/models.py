from django.db import models


class Persona(models.Model):
    # Datos Principales (Usados en Portada e Index)
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    profesion = models.CharField(max_length=100, verbose_name="Profesión (Subtítulo Portada)")

    # Biografía (Usados en Acerca de / About)
    biografia = models.TextField(verbose_name="Biografía Corta")
    biografia_extra = models.TextField(verbose_name="Biografía Extra (Opcional)", blank=True, null=True)
    foto = models.ImageField(upload_to='persona', verbose_name="Foto de Perfil (Avatar)", blank=True, null=True)

    # Datos de Contacto (Usados en Contacto / Contact y Base)
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    descripcion_contacto = models.TextField(verbose_name="Descripción sección Contacto")
    honorarios = models.CharField(max_length=100, verbose_name="Honorarios", blank=True, null=True)

    # Enlaces de Redes Sociales (Usados en el Pie de Página / Base)
    github = models.URLField(verbose_name="Enlace de GitHub", blank=True, null=True)
    youtube = models.URLField(verbose_name="Enlace de YouTube", blank=True, null=True)
    instagram = models.URLField(verbose_name="Enlace de Instagram", blank=True, null=True)
    tiktok = models.URLField(verbose_name="Enlace de TikTok", blank=True, null=True)

    class Meta:
        verbose_name = "Datos Personales"
        verbose_name_plural = "Datos Personales"

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
