from django.urls import path

import schedule.views

app_name = "schedule"
urlpatterns = [
    path("categories/",schedule.views.categories,name="categories"),
    path("categories/<int:id>/",schedule.views.category,name="category"),
    path("tasks/",schedule.views.tasks,name="tasks"),
    path("tasks/<int:id>/",schedule.views.tasks,name="task")
]