from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Sales)
admin.site.register(Products)
