from django.db import models
from account.models import CustomUser


class Todo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=350)
    subtext = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title