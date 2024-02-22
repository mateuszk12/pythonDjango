
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from .views import custom404,custom400,custom403,custom500

handler400 = custom400
handler403 = custom403
handler404 = custom404
handler500 = custom500
urlpatterns = [
    path('api_schema/', get_schema_view(
        title='DOCS',
        public=True
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('schedule/',include("schedule.urls")),
    path('auth/', include("apiAuth.urls"))
]
