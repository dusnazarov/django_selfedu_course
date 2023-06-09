from django.urls import path
from . import views


urlpatterns=[        
    path('', views.post_page, name='home'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('post/<int:post_id>/',views.read_post, name='post'),
    path('add_post/',views.add_post, name='add_post'),             
  
                  
    path('about/', views.about, name='about'), 
    path('contact/',views.contact, name='contact'),    
    path('login/',views.login, name='login'),          
           

]

