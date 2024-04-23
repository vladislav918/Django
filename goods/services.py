from django.db.models import Q

from .models import Comment, Product


def get_comments(product, request):
    """ Возвращает комментарии сортированные по дате """
    sort_by = request.GET.get('sort_by', 'created_at')
    sort_dir = request.GET.get('sort_dir', 'desc')

    if sort_by == 'created_at':
        if sort_dir == 'asc':
            comments = Comment.objects.filter(
                product=product
            ).order_by('created')
        else:
            comments = Comment.objects.filter(
                product=product
            ).order_by('-created')
    else:
        comments = Comment.objects.filter(
            product=product
        ).order_by('-created')

    return comments


def get_product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.filter(available=True)

    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) | 
            Q(article_number__exact=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    return products

