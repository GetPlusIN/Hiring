from django.contrib import admin
from .models import Book


#Register your model to view in admin panle
admin.site.register(Book)