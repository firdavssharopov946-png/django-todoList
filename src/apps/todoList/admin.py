from django.contrib import admin  # noqa
from apps.todoList.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    list_display=['title', 'dedline']

