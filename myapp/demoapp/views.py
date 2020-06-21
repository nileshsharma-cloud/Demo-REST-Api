from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import employeeSerializer
from .models import Employees
from rest_framework.response import Response

# Create your views here.

class EmployeeViewSet(APIView):

    def get(self, request):
        employees1 = Employees.objects.all()
        serializer = employeeSerializer(employees1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

