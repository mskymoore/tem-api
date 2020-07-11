from rest_framework import serializers
from temapi.models import EntryDate

class EntryDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryDate
        fields = ('date',)

