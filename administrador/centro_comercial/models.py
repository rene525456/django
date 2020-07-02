from django.db import models

class CentroComercial(models.Model):
    name = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name = "Centro Comercial"
        verbose_name_plural = "Centros Comerciales"

    def __str__(self):
        return self.name

class CategoriaLocal(models.Model):
    name = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name = "Categoria del Local"
        verbose_name_plural = "Categorias de los Locales"

    def __str__(self):
        return self.name

class Local(models.Model):
    name = models.CharField(max_length = 100)
    centro_comercial = models.ForeignKey(CentroComercial, on_delete=models.CASCADE,
                        related_name='locales_centro_comercial',
                        verbose_name='Centro Comercial')
    categoria_local = models.ManyToManyField(CategoriaLocal,
                        related_name='categoria_local',
                        verbose_name='Categorias del Local')
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"

    def __str__(self):
        return self.name