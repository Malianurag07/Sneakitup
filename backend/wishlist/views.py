from django.shortcuts import render, redirect, get_object_or_404
from products.models import Shoe
from cart.cart import Cart
from .wishlist import Wishlist


def wishlist_detail(request):
    """
    Displays all items currently in the user's wishlist.
    """
    wishlist = Wishlist(request)
    return render(request, 'wishlist/detail.html', {'wishlist': wishlist})


def wishlist_add(request, pk):
    """
    Adds a product to the wishlist.
    """
    wishlist = Wishlist(request)
    product = get_object_or_404(Shoe, id=pk)
    wishlist.add(product)
    return redirect('wishlist:wishlist_detail')


def wishlist_remove(request, pk):
    """
    Removes a product from the wishlist.
    """
    wishlist = Wishlist(request)
    product = get_object_or_404(Shoe, id=pk)
    wishlist.remove(product)
    return redirect('wishlist:wishlist_detail')


def move_to_cart(request, pk):
    """
    Moves a product from wishlist to cart.
    """
    wishlist = Wishlist(request)
    cart = Cart(request)
    product = get_object_or_404(Shoe, id=pk)

    # Add product to cart
    cart.add(product=product, quantity=1, update_quantity=False)

    # Remove product from wishlist
    wishlist.remove(product)

    # Redirect to cart page
    return redirect('cart:cart_detail')
