from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Libro
        #indicamos que use todos los campos 
        fields = "__all__"
        #les decimos cuales son los de solo lectura 
        read_only_fields = ( "id", "created_at", "updated_at", ) 