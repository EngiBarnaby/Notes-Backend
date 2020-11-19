from django.db import models

class Api(models.Model):
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.url
