from django.db import models

# Create your models here.
class Libro(models.Model): 
    title = models.CharField(max_length=255) 
    genre = models.CharField(max_length=255) 
    year = models.CharField(max_length=4) 
    author = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta: 
        ordering = ("-created_at",) 
        verbose_name = "Libro" 
        verbose_name_plural = "Libros" 

    def __str__(self): 
        return self.title