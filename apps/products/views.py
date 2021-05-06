from django.views import generic
from django.urls import reverse

from .models import Product
from .forms import ProductForm


class ProductList(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreate(generic.CreateView):
    form_class = ProductForm
    template_name = 'products/product_create.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})
