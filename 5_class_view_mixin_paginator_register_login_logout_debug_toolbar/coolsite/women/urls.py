from django.urls import path
from . import views


urlpatterns = [        
    path('', views.PostPage.as_view(), name='home'),
    path('category/<slug:cat_slug>/', views.ShowCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', views.ReadPost.as_view(), name='post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/',views.LoginUser.as_view(), name='login'),                
    path('logout/',views.logout_user, name='logout'),                
  
                  
    path('about/', views.about, name='about'), 
    path('contact/',views.contact, name='contact'),    
           
         
   

]

