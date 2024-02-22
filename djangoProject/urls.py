
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/',include("schedule.urls")),
    path('account/',include("accounts.urls"))
]
urlpatterns = format_suffix_patterns(urlpatterns)