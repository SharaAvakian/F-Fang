from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def home(request):
    featured = Product.objects.filter(is_active=True, is_featured=True)[:6]
    categories = Category.objects.all()
    latest = Product.objects.filter(is_active=True)[:8]
    return render(request, 'home/index.html', {
        'featured': featured,
        'categories': categories,
        'latest': latest,
    })


def product_list(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()

    category_slug = request.GET.get('category')
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', '-created_at')

    if category_slug:
        products = products.filter(category__slug=category_slug)

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    sort_map = {
        'price_asc': 'price',
        'price_desc': '-price',
        'name': 'name',
        '-created_at': '-created_at',
    }
    products = products.order_by(sort_map.get(sort, '-created_at'))

    active_category = None
    if category_slug:
        active_category = Category.objects.filter(slug=category_slug).first()

    return render(request, 'products/list.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'sort': sort,
        'active_category': active_category,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    variants = product.variants.all()
    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(id=product.id)[:4]

    sizes = variants.values_list('size', flat=True).distinct()
    colors = variants.values_list('color', flat=True).distinct()

    return render(request, 'products/detail.html', {
        'product': product,
        'variants': variants,
        'related': related,
        'sizes': sizes,
        'colors': colors,
    })
