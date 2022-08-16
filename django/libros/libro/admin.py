from django.contrib import admin
from .models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
     readonly_fields = ('created_at', 'updated_at')
     list_display = ('title', 'year', 'author')