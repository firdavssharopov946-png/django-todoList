from django.contrib import admin  # noqa
from apps.todoList.models import Todo
from apps.todoList.resources import TodoResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Todo)
class TodoModelAdmin(ImportExportModelAdmin):
    list_display=['title', 'dedline']
    resource_classes= [TodoResource]

