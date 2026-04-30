from django.contrib import admin  # noqa
from apps.todoList.models import User
from apps.users.resources import UserResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(User)
class UserModelAdmin(ImportExportModelAdmin):
    list_display=['first_name', 'last_name']
    resource_classes = [UserResource]

