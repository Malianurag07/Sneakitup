from django.shortcuts import render, get_object_or_404
from .models import Shoe

# --- Homepage View ---
def home_page(request):
    first_shoe = Shoe.objects.first()
    context = {
        'shoe': first_shoe,
    }
    return render(request, 'products/home.html', context)

# --- Shop Page View ---
def shop_page(request):
    all_shoes = Shoe.objects.all()
    context = {
        'shoes': all_shoes,
    }
    return render(request, 'products/shop.html', context)

# --- NEW: Product Detail Page View ---
def product_detail_page(request, pk):
    product = get_object_or_404(Shoe, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)



