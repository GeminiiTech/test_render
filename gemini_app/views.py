from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def home(request):
    data = {
        "Name":"Kehinde",
        "Phone":"08116354898",
    }
    return Response(data)
