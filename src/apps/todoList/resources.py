from import_export import resources
from apps.todoList.models import Todo


class TodoResource(resources.ModelResource):
    class Meta:
        model = Todo