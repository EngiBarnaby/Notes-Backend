from django.shortcuts import render

from .models import Note

def index(request):
    all_notes = Note.objects.all()
    context = {"notes": all_notes}
    return render(request, "note/main.html", context)