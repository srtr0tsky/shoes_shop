from django.shortcuts import render, get_object_or_404, redirect
from .models import ShoppingCartDatabase
from product.models import Product
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def add_to_cart(request, slug):
    context = {}
    if slug != ' ':
        obj = get_object_or_404(Product, slug=slug)
        query = ShoppingCartDatabase.objects.filter(product=obj)
        if not query:
            ShoppingCartDatabase(product=obj.product_name,
                                 price=obj.price,
                                 slug=slug,
                                 user_id=request.user.id).save()
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request, template_name='shopping-cart.html', context=context)

@login_required(login_url='/accounts/login/')
def remove_from_cart(request, slug):
    product_name = get_object_or_404(Product, slug=slug)
    obj_cart = get_object_or_404(ShoppingCartDatabase, product=product_name)
    ShoppingCartDatabase.objects.filter(product=obj_cart.product).delete()
    return redirect(request.META.get('HTTP_REFERER'))

class ShowItemsCart(LoginRequiredMixin, ListView):
    template_name = 'shopping-cart.html'
    model = ShoppingCartDatabase

    def get_queryset(self):
        query = super(ShowItemsCart, self).get_queryset()
        return query.filter(user_id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowItemsCart, self).get_context_data()
        database = super(ShowItemsCart, self).get_queryset()
        all_price = database.values_list('price').all()

        return context



