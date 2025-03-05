from django.urls import path
from .views import ReminderList, ReminderCreate, ReminderUpdate, ReminderDelete

urlpatterns = [
    path('', ReminderList.as_view(), name='reminder_list'),
    path('create/', ReminderCreate.as_view(), name='reminder_create'),
    path('<int:pk>/update/', ReminderUpdate.as_view(), name='reminder_update'),
    path('<int:pk>/delete/', ReminderDelete.as_view(), name='reminder_delete'),
]
