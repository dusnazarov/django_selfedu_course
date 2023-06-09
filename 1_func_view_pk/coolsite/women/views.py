from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound
from .models import Women, Category
from .forms import AddPostForm



menu = [
    {'title':"About site",'url_name':'about'},
    {'title':"Add statie",'url_name':'add_post'},
    {'title':"Back connection",'url_name':'contact'},
    {'title':"Enter",'url_name':'login'},

]
    
def post_page(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
  
    context = {
        'posts':posts, 
        'title':'Home Page',    
        'menu':menu,
        'cats':cats
    }        
      
    return render(request, 'women/post_page.html', context=context)



def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    # print(posts)

    if len(posts)==0:
        raise Http404
        
    context = {
        'posts':posts,        
        'menu':menu,
        'title':'Inner page',
        'cats':cats
     
    }

    return render(request, 'women/post_page.html', context=context)

def read_post(request, post_id):
    cats= Category.objects.all()
    post = get_object_or_404(Women, pk=post_id)
       
    # print(post)
    # print(post_id)

    context = {
        'post':post,
        'menu':menu,
        'title':post.title,
        'cats':cats  
       
    }

    return render(request, 'women/read_post.html', context=context)

def add_post(request):
    if request.method=='POST':
        form=AddPostForm(request.POST, request.FILES)
        if form.is_valid():
           
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form=AddPostForm()
    return render(request, 'women/add_post.html', {'form':form, 'menu':menu, 'title':'Add Page'})




def about(request):
    return render(request, 'women/about.html', {'menu':menu,'title':'about site'})


def contact(request):
     return HttpResponse("Back connection")

def login(request):
    return HttpResponse("Authentication")

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page NOt Found</h1>')








