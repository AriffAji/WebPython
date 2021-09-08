from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *
# from buku.resource import BukuResource

# Create your views here.

# def index(request):
#     context = {
#         'title' : 'Index'
#     }
#     template_name = None
#     if request.user.is_authenticated:
#         template_name = 'login.html'
#     else:
#         template_name = 'index_anon.html'
#     return render(request, template_name, context)

def index(request):
    context = {
        'title' : 'Login'
    }
    user = None
        #   (ketika user buka superuser 
        #  # if not request.user.is_superuser:
        #     #     return redirect('logout')
        #     # else:
        #     #     raise Http404)

    #logika akses akun menggunakan django
    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username = username_login, password = password_login)
        if user is not None:
            login(request, user)
            return redirect('buku')
        else:
            messages.error(request, "Anda Tidak Mempunyai Akun")
            return redirect('login')

   #logika untuk membuat agar setelah login tidak measuk ke haalama login       
    if request.method == "GET":
        if request.user.is_authenticated:
            #untuk user
            return redirect('buku')
        else:
            #untuk anonymousUser
            return render(request, 'login.html', context)

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Dibuat!")
            return redirect('index')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        context = {
            'title' : 'SignUp',
            'form' : form,
        }
    return render(request, 'signup.html', context)

@login_required(login_url='index') 
def buku(request):
    books = Buku.objects.all()
    context = {
        'title' : 'Buku',
        'judul' : 'ini adalah buku',
        'bukutok' : books,
    }
    print(request.user)
    return render(request, 'buku.html', context)

@login_required(login_url='index')
def penerbit(request):
    context = {
        'title' : 'Penerbit',
        'judul' : 'ini adalah penerbit'
    }
    return render(request, 'penerbit.html', context)


@login_required(login_url='index') 
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()

            context = {
                'form' : form,
            }
            messages.success(request, "Data Berhasil Disimpan")
            return render(request, 'tambah-buku.html', context)

    else:
        form = FormBuku()
        context = {
            'form' : form,
        }
    return render(request, 'tambah-buku.html', context)

@login_required(login_url='index')
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data Berhasil Dihapus")
    return redirect('buku')

@login_required(login_url='index')
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubahbuku.html'
    if request.POST:
        form = FormBuku(request.POST,request.FILES, instance=buku)
        if form.is_valid():
           form.save()
           messages.success(request, "Data Berhasil Tersimpan")
           return redirect('ubah_buku', id_buku=id_buku)
    
    else:
        form = FormBuku(instance=buku)
        context = {
            'form' : form,
            'buku' : buku,
        }
    return render(request, template, context)

@login_required(login_url='index')
def logOut(request):
    context = {
        'title' : 'logout'
    }
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
        return redirect('index')
           
    return render(request, 'logout.html', context)

# def export_xls(request):
#     buku = BukuResource()
#     dataset = buku.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=buku.xls'
#     return response
