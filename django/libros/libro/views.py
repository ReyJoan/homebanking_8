from django.shortcuts import render

# Create your views here.




from django.http import JsonResponse
from libro.models import Libro
from libro.serializers import LibroSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
def testSerializers(request):
    libro1 = Libro.objects.get(id=1)
    serializer = LibroSerializer(libro1)
    return JsonResponse(serializer.data)