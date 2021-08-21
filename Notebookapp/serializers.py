from rest_framework import serializers
from .models import  BooksModel

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'