from schedule.models import Category,Task
from schedule.serializers import CategorySerializer,TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework import generics

class Categories(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class Category(generics.GenericAPIView,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
class Tasks(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class Task(generics.GenericAPIView,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)