from rest_framework.generics import ListAPIView, RetrieveAPIView
from temapi.models import EntryDate
from .serializers import EntryDateSerializer
from django.http import HttpResponse
import json


class EntryDateListView(ListAPIView):
    queryset = EntryDate.objects.all()
    serializer_class = EntryDateSerializer
    

class EntryDateDetailView(RetrieveAPIView):
    queryset = EntryDate.objects.all()
    serializer_class = EntryDateSerializer


class EntryDateYearView(ListAPIView):
    serializer_class = EntryDateSerializer

    def get_queryset(self):
        
        if 'year' in self.kwargs:
            return EntryDate.objects.filter(
                        date__year=self.kwargs['year']
                   )
        
        else:
            return EntryDate.objects.none()