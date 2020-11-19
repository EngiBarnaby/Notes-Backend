from django.db import models

class NoteCategory(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title
