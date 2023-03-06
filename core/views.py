
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    CreateView)
from cart.models import ShoppingCartDatabase
from product.models import Product
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
class MainPage(ListView):
    template_name = 'index.html'
    model = Product


@login_required(login_url='/accounts/login/')
class DetailProduct(DetailView):
    template_name = 'detail-product.html'
    model = Product
    def get_context_data(self, **kwargs):
        data = super(DetailProduct, self).get_context_data()
        obj = get_object_or_404(Product, slug=self.kwargs['slug'])
        query = ShoppingCartDatabase.objects.filter(product=obj)
        if query:
            in_cart = True
        else:
            in_cart = False
        data.update({'in_cart': in_cart})
        return data






























