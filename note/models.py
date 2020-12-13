from django.db import models

from tinymce.models import HTMLField

from account.models import CustomUser


class NoteCategory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=150)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    content = HTMLField(blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
