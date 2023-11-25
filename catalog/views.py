
from django.shortcuts import get_object_or_404, render

from config.settings import PAGINATE_BY
from _utils.utils import get_foto_list, get_pagination

from .models import Product, ProductCategory


def product_list(request):

    product_list = Product.objects.filter(is_publish=True)
    object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, product_list, PAGINATE_BY)

    return render(
        request,
        'catalog/product_list.html',
        context={
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url
        })


def search_product_list(request):

    search = request.GET.get('search', '')

    if search:
        product_list = Product.objects.filter(title__icontains=search, is_publish=True)
        product_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, product_list, PAGINATE_BY)

    else:
        product_list = Product.objects.filter(is_publish=True)
        object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, product_list, PAGINATE_BY)

    return render(
        request,
        'catalog/product_list.html',
        context={
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url
        })


def cat_category_list(request):
    category_list = Product.objects.filter(is_publish=True)

    return render(
        request,
        'catalog/category_list.html',
        context={
            'category_list': category_list,
        })


def category_detail(request, slug):
    category = ProductCategory.objects.filter(slug=slug).first()

    product_list = Product.objects.filter(category_id=category.id).all()
    object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, product_list, PAGINATE_BY)

    return render(
        request,
        'catalog/category_detail.html',
        context={
            'category': category,
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url,
        })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    image_list = get_foto_list(product)

    product_next = Product.objects.filter(date_update__gt=product.date_update).order_by('date_update').first()
    product_previos = Product.objects.filter(date_update__lt=product.date_update).order_by('-date_update').first()

    related_product_list = Product.objects.filter(
        is_publish=True,
        category_id=product.category).order_by('?').exclude(pk=product.pk)[:6]

    return render(
        request,
        'catalog/product_detail.html',
        context={
            'product': product,
            'image_list': image_list,

            'product_next': product_next,
            'product_previos': product_previos,

            'related_product_list': related_product_list
        })
