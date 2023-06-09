from .models import Category

menu = [
    {'title':"About site",'url_name':'about'},
    {'title':"Add statie",'url_name':'add_post'},
    {'title':"Back connection",'url_name':'contact'},
 
]

class DataMixin:
    paginate_by = 2  
    
    def get_user_context(self,**kwargs):
        cats = Category.objects.all()
        context = kwargs
        
        new_menu = menu.copy()

        if not self.request.user.is_authenticated:
            new_menu.pop(1)
            
        context['menu'] = new_menu
         
        context['cats'] = cats 
        return context