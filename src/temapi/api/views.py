from rest_framework.generics import ListAPIView, RetrieveAPIView
from temapi.models import EntryDate
from .serializers import EntryDateSerializer
from django.http import HttpResponse
import json


# class CaseTypeListView(ListAPIView):
#     serializer_class = CaseTypeSerializer
# 
#     def get_queryset(self):
#         if 'hash' in self.kwargs:
#             return CaseType.objects.filter(
#                 location__friendly_hash=self.kwargs['hash']
#             )

class EntryDateListView(ListAPIView):
    queryset = EntryDate.objects.all()
    serializer_class = EntryDateSerializer
    

class EntryDateDetailView(RetrieveAPIView):
    queryset = EntryDate.objects.all()
    serializer_class = EntryDateSerializer

