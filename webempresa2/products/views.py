from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductImages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})

def detail(request,id):
    product=get_object_or_404(Product, id=id)
    images=ProductImages.objects.filter(product_id=id)
    context={'product':product,
             'images':images,
             }
    return render(request,"products/detail.html",context)
   

def categories_m(request):
    query_Set = Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(query_Set, 20)
    try:
        cat = paginator.page(page)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.page(paginator.num_pages)
    return render(request, 'products/categories.html', {'categories': cat})