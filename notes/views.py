from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm

class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/note_list.html"
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note_list")
