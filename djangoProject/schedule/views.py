from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from schedule.models import Category,Task
from schedule.serializers import CategorySerializer,TaskSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def categories(request):
    if request.method == 'GET':
        categoriesRes = Category.objects.all()
        catSerialized = CategorySerializer(categoriesRes, many=True)
        return JsonResponse({"categories":catSerialized.data})
    if request.method == 'POST':
        addCategory = CategorySerializer(data=request.data)
        if addCategory.is_valid():
            addCategory.save()
            return Response(addCategory.data,status=status.HTTP_201_CREATED)
@api_view(['PUT','DELETE'])
def category(request,id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        changeCategory = CategorySerializer(category,data=request.data)
        if changeCategory.is_valid():
            changeCategory.save()
        return Response(changeCategory,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def tasks(request):
    if request.method == 'GET':
        tasksRes = Task.objects.all()
        taskSerialized = TaskSerializer(tasksRes, many=True)
        return JsonResponse({"tasks": taskSerialized.data})
    if request.method == 'POST':
        addTask = TaskSerializer(data=request.data)
        if addTask.is_valid():
            addTask.save()
            return Response(addTask.data,status=status.HTTP_201_CREATED)
@api_view(['PUT','DELETE'])
def task(request,id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        changeTask = TaskSerializer(task,data=request.data)
        if changeTask.is_valid():
            changeTask.save()
        return Response(changeTask,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_200_OK)