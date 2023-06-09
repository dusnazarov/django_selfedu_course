from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseNotFound
from .models import Women
from django.views.generic import ListView, DetailView, CreateView 
from .forms import AddPostForm
from django.urls import reverse_lazy
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin



class PostPage(DataMixin, ListView):
    model = Women
    template_name = 'women/post_page.html'
    context_object_name = 'posts'
  
       
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_data = self.get_user_context(title='Home Page')
        new_context = dict(list(context.items()) + list(mixin_data.items()))               
        return new_context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


class ShowCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/post_page.html'
    context_object_name = 'posts'
    allow_empty = False    
    

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self,*, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)        
        mixin_data = self.get_user_context(title='Category -'  + str(context['posts'][0].cat))
        new_context = dict(list(context.items()) + list(mixin_data.items()))
        return new_context


class ReadPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/read_post.html' 
    context_object_name = 'post'    
    slug_url_kwarg = 'post_slug'
    
 
    def get_context_data(self,*, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs) 
        mixin_data = self.get_user_context(title='Read Post')
        new_context = dict(list(context.items()) + list(mixin_data.items()))
        return new_context


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_post.html'
    success_url = reverse_lazy('home')  
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)       
        mixin_data = self.get_user_context(title='Add Post')
        new_context = dict(list(context.items()) + list(mixin_data.items()))      
        return new_context



def about(request):
    return render(request, 'women/about.html', {'title':'about site'})

def contact(request):
     return HttpResponse("Back connection")

def login(request):
    return HttpResponse("Authentication")

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page NOt Found</h1>')
