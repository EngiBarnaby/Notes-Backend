from django.contrib import admin

from .models import Step, Project, TestRecursion

class StepInline(admin.StackedInline):
    model = Step

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        StepInline,
    ]

admin.site.register(Step)
admin.site.register(Project, ProjectAdmin)
admin.site.register(TestRecursion)