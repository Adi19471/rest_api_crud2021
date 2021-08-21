from django.contrib import admin

# Register your models here.
from .models import BooksModel

admin.site.register(BooksModel)