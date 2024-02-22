from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,username=request.data['username'])
    if user.check_password(request.data['password']):
        token,created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    return Response(user)
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password((request.data['password']))
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
