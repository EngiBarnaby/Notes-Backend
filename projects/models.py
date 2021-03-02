from django.db import models

from account.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=150, blank=False)
    project_description = models.CharField(max_length=250, blank=True, null=True)
    project_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-project_created"]

    def __str__(self):
        return self.name

class Step(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    step_created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', verbose_name="Родитель",
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True,
                                   related_name="sub_steps"
                               )

    class Meta:
        ordering = ["step_created"]

    def __str__(self):
        return self.title



class TestRecursion(models.Model):
    title = models.CharField(max_length=150, blank=False)
    parent = models.ForeignKey('self', verbose_name="Родитель",
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                related_name="children")

    def __str__(self):
        return self.title