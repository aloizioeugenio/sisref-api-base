from django.shortcuts import render
from app.models import Tabsetor
from app.models import Servativ
from app.serializers import TabSetorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.serializers import ServativSerializer

@api_view(['GET'])
def tabsetor_list(request):
    tabsetor = Tabsetor.objects.first()
    serializer = TabSetorSerializer(tabsetor)
    return Response(serializer.data)

@api_view(['GET'])
def servativ_list(request):
    servativ = Servativ.objects.first()
    serializer = ServativSerializer(servativ)
    return Response(serializer.data)

@api_view(['GET'])
def tabsetor_detail_change_and_delete(request, codigo):
    try:
        tabsetor = Tabsetor.objects.get(codigo=codigo)
    except tabsetor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TabSetorSerializer(tabsetor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TabSetorSerializer(tabsetor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tabsetor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def servativ_detail_change_and_delete(request, mat_siape):
    try:
        servativ = Servativ.objects.get(mat_siape=mat_siape)
    except servativ.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ServativSerializer(servativ)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ServativSerializer(servativ, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        servativ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)