from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='portfolio')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('created',)
        db_table = 'portfolio'

    def __str__(self):
        return self.title

