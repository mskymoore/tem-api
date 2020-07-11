from django.urls import path
from .views import EntryDateListView, EntryDateDetailView, EntryDateYearView

urlpatterns = [
   path('ed', EntryDateListView.as_view()),
   path('ed/<pk>', EntryDateDetailView.as_view()),
   path('ed/yr/<year>', EntryDateYearView.as_view())
]