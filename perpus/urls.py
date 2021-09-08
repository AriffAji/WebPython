"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from buku.views import *
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth.views import loginView
from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    # path('login/', login, name='login'),
    path('logout/', logOut, name='logout'),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambahbuku/', tambah_buku),
    path('tambah_buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>/', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>/', hapus_buku, name='hapus_buku'),
    # path('export/xls/', export_xls, name='export_xls'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

