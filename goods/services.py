from .models import Comment


def get_comments(product, request):
    """ Возвращает комментарии сортированные по дате """
    sort_by = request.GET.get('sort_by', 'created_at')
    sort_dir = request.GET.get('sort_dir', 'desc')

    if sort_by == 'created_at':
        if sort_dir == 'asc':
            comments = Comment.objects.filter(product=product).order_by('created')
        else:
            comments = Comment.objects.filter(product=product).order_by('-created')
    else:
        comments = Comment.objects.filter(product=product).order_by('-created')

    return comments
