from django.http import HttpResponse
from django.shortcuts import render
from shopapp.models import Product, Category
from django.db.models import Q


# Create your views here.
def SearchResult(request):
    products = None
    query = None
    category = None
    product_cat = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        category = Category.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        
        if category:
            for i in category:
                product_cat = Product.objects.all().filter(category__in=category)
        return render(request, 'search.html', {'query': query, 'products': products, 'category': category, 'product_cat':product_cat})

