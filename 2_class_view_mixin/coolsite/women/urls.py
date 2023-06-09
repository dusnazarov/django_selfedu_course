from django.urls import path
from . import views


urlpatterns=[        
    path('', views.PostPage.as_view(), name='home'),
    path('category/<slug:cat_slug>/', views.ShowCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', views.ReadPost.as_view(), name='post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),              
  
                  
    path('about/', views.about, name='about'), 
    path('contact/',views.contact, name='contact'),    
    path('login/',views.login, name='login'),          
   

]

