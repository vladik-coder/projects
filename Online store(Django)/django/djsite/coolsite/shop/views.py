from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ShopHome(ListView):
    model = Kazan
    template_name='shop/index.html'
    context_object_name = 'kazans'

    def get_queryset(self):
        return Kazan.objects.filter(is_published=True)

# def index(request):
#     kazans = Kazan.objects.all()
#     return render(request,'shop/index.html', {'kazans': kazans})

def about(request,post_id):
    kazans=Kazan.objects.all()
    return render(request,'shop/about.html', {'kazans': kazans, 'post_id': post_id})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'shop/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items()) + list(c_def.items()))