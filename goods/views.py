from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .models import Product
from .forms import CommentForm
from .services import get_comments


class ProductsView(ListView):
    model = Product
    template_name = 'goods/product_list.html'


class ProductDetalView(FormMixin, DetailView):
    model = Product
    context_object_name = 'goods'
    form_class = CommentForm
    success_url = '#'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        comments = get_comments(product, self.request)
        context['comments'] = comments
        context['form'] = CommentForm()
        return context
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.product = self.get_object()
        comment.save()
        return super().form_valid(form)
