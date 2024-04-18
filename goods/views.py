from django.views.generic import DetailView, ListView, CreateView

from .models import Product
from .forms import CommentForm
from .services import get_comments


class ProductsView(ListView):
    model = Product
    template_name = 'goods/product_list.html'


class ProductDetalView(DetailView):
    model = Product
    context_object_name = 'goods'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        comments = get_comments(product, self.request)
        context['comments'] = comments
        context['form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = "goods/comment_form.html"
