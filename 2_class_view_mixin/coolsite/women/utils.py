# from .models import Category

# menu = [
#     {'title':"About site",'url_name':'about'},
#     {'title':"Add statie",'url_name':'add_post'},
#     {'title':"Back connection",'url_name':'contact'},
#     {'title':"Enter",'url_name':'login'},

# ]

# class DataMixin:
#     def get_user_context(self,**kwargs):
#         context = kwargs 
#         cats = Category.objects.all()        
#         context['menu'] = menu
#         context['cats'] = cats 
#         return context


from .models import Category

menu = [
    {'title':"About site",'url_name':'about'},
    {'title':"Add statie",'url_name':'add_post'},
    {'title':"Back connection",'url_name':'contact'},
    {'title':"Enter",'url_name':'login'},

]

class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs 
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
       
        context['cats'] = cats 
        return context