from django.shortcuts import  render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from .models import Women, Category 
from django.views.generic import ListView, DetailView,CreateView 
from .forms import AddPostForm
from django.urls import reverse_lazy


menu = [
    {'title':"About site",'url_name':'about'},
    {'title':"Add statie",'url_name':'add_post'},
    {'title':"Back connection",'url_name':'contact'},
    {'title':"Enter",'url_name':'login'},

]



class PostPage(ListView):
    model = Women
    template_name = 'women/post_page.html'
    context_object_name = 'posts'
    cats = Category.objects.all()

    def get_queryset(self):
        return Women.objects.filter(is_published=True)
   
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['menu'] = menu
        context['title'] = 'Home Page' 
        context['cats'] = self.cats       
        # print(context['posts'])       
        # print(context['cats'])            
        return context


class ShowCategory(ListView):
    model = Women
    template_name = 'women/post_page.html'
    context_object_name = 'posts'
    cats = Category.objects.all()    
    allow_empty = False
    
    

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self,*, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)        
        context['menu'] = menu  
        context['title']='Category-' + str(context['posts'][0].cat)        
        context['cats'] = self.cats
        return context


class ReadPost(DetailView):
    model = Women
    template_name = 'women/read_post.html' 
    context_object_name = 'post'   
    cats = Category.objects.all()    
    slug_url_kwarg = 'post_slug'
    
 
    def get_context_data(self,*, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)         
        context['cats'] = self.cats        
        # print(context['post'])        
        return context


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'women/add_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu     
        return context



def about(request):
    return render(request, 'women/about.html', {'menu':menu,'title':'about site'})

def contact(request):
     return HttpResponse("Back connection")

def login(request):
    return HttpResponse("Authentication")

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page NOt Found</h1>')








