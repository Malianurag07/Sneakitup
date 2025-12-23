from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Shoe
from .cart import Cart
from .forms import CartAddProductForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Shoe
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def add_to_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Shoe, id=pk)
    form = CartAddProductForm(request.POST)

    print("DEBUG: Received POST:", request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        size = request.POST.get('size', '')
        print("DEBUG: Adding product:", product.name, "size:", size)
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update'],
            size=size
        )
        print("DEBUG: Session cart after add:", request.session.get('cart'))
    else:
        print("DEBUG: Form not valid:", form.errors)

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True}
        )
    sizes = ['6', '7', '8', '9', '10']
    return render(request, 'cart/detail.html', {'cart': cart, 'sizes': sizes})

def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Shoe, id=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')
def test_session(request):
    print("DEBUG: Current session keys:", request.session.keys())
    print("DEBUG: CART SESSION:", request.session.get('cart'))
    return render(request, 'cart/detail.html', {'cart': Cart(request)})



