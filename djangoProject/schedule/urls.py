from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import schedule.views

app_name = "schedule"
urlpatterns = [
    path("categories/",schedule.views.Categories.as_view(),name="categories"),
    path("categories/<int:pk>/",schedule.views.SingleCategory.as_view(),name="category"),
    path("tasks/",schedule.views.Tasks.as_view(),name="tasks"),
    path("tasks/<int:pk>/",schedule.views.Task.as_view(),name="task")
]
# urlpatterns = format_suffix_patterns(urlpatterns)