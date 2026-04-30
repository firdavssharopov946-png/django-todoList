from django.db import models
from apps.users.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    is_complated = models.BooleanField(default=False)
    dedline = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.title}"
