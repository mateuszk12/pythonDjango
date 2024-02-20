from django.urls import path

import schedule.views


urlpatterns = [
    path("categories/",schedule.views.categories,name="categories"),
    path("tasks/",schedule.views.tasks,name="tasks")
]