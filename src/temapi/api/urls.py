from django.urls import path
from .views import EntryDateListView, EntryDateDetailView

urlpatterns = [
   path('ed/<pk>', EntryDateListView.as_view()),
   path('edd/<pk>', EntryDateDetailView.as_view())
]