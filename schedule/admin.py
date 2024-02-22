from django.contrib import admin
from schedule.models import Category
from schedule.models import Task
# Register your models here.
admin.site.register(Task)
admin.site.register(Category)