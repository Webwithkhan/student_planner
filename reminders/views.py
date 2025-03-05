from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Reminder
from .forms import ReminderForm

class ReminderList(LoginRequiredMixin, ListView):
    model = Reminder
    template_name = "reminders/reminder_list.html"

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

class ReminderCreate(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = "reminders/reminder_form.html"
    success_url = reverse_lazy("reminder_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReminderUpdate(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = "reminders/reminder_form.html"
    success_url = reverse_lazy("reminder_list")

class ReminderDelete(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = "reminders/reminder_confirm_delete.html"
    success_url = reverse_lazy("reminder_list")
