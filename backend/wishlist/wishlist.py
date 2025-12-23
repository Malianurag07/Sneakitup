# wishlist/wishlist.py
from products.models import Shoe

class Wishlist:
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get('wishlist')
        if not wishlist:
            wishlist = self.session['wishlist'] = {}
        self.wishlist = wishlist

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'image': product.main_image.url if product.main_image else ''
            }
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.wishlist.keys()
        products = Shoe.objects.filter(id__in=product_ids)
        for product in products:
            item = self.wishlist[str(product.id)]
            item['product'] = product
            yield item

    def clear(self):
        self.session['wishlist'] = {}
        self.save()
