from django.shortcuts import render
from django.http import JsonResponse
from .serializers import NameSerializer
from  .models import MyName
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def name_list(request):
    if request.method == 'GET':
        names = MyName.objects.all()
        serializer = NameSerializer(names, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def name_detail(request, pk):
    try:
        names = MyName.objects.get(pk=pk)
    except MyName.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NameSerializer(names)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NameSerializer(names, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        names.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

