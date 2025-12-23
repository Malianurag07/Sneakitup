# backend/products/models.py
from django.db import models

class Shoe(models.Model):
    # --- Core Information ---
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True) # blank=True means this is optional

    # We use DecimalField for money to avoid rounding errors
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    # 'stock_quantity' stores how many we have. 
    # 'default=0' means if we don't set it, it's 0
    stock_quantity = models.IntegerField(default=0)

    # --- For the "Shop" Page ---
    # This will be the main image shown on the product grid
    # 'upload_to' tells Django to save these images in a folder called 'shoe_images'
    main_image = models.ImageField(upload_to='shoe_images/', null=True, blank=True)

    # --- For the "Customizer" Feature ---
    # is_customizable = models.BooleanField(default=False)
    # base_image = models.ImageField(upload_to='base_shoe_images/', null=True, blank=True)

    # --- Timestamps (Good Practice) ---
    # 'auto_now_add' sets the create date on the first save
    created_at = models.DateTimeField(auto_now_add=True)
    # 'auto_now' updates this field every time the model is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # This tells Django what to show in the admin panel (e.g., "Air Max 1")
        return self.name