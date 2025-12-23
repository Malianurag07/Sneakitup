# backend/products/admin.py

from django.contrib import admin
from .models import Shoe  # <-- 1. Import your Shoe model

# 2. Register your model
admin.site.register(Shoe)