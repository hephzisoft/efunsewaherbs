from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Product
from django.db.models import Q


class HomeView(View):
    template_name = 'main/home.html'

    def get(self, request):
        q = request.GET.get('q')
        if q:
            products = Product.objects.filter(Q(name__icontains=q))
        else:
            products = Product.objects.all()

        return render(request, self.template_name, {'products': products})


class ProductView(View):
    template_name = 'main/product-details.html'

    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        return render(request, self.template_name, {'product': product})


def about(request):
    return render(request, 'main/about.html')
