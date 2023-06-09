
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from coolsite import settings
from women.views import PageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),

]

handler404=PageNotFound

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


