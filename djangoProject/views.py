from django.http import JsonResponse
from rest_framework import status

def custom404(request, exception=None):
    return JsonResponse({
        'error': 'The resource was not found'
    },status=status.HTTP_404_NOT_FOUND)
def custom403(request, exception=None):
    return JsonResponse({
        'error': 'operation forbidden'
    },status=status.HTTP_403_FORBIDDEN)
def custom400(request, exception=None):
    return JsonResponse({
        'error': 'bad request'
    },status=status.HTTP_400_BAD_REQUEST)
def custom500(request, exception=None):
    return JsonResponse({
        'error': 'internal server error'
    },status=status.HTTP_500_INTERNAL_SERVER_ERROR)