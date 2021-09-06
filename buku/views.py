from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data Berhasil Dihapus")
    return redirect('buku')


def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubahbuku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
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

def buku(request):
    books = Buku.objects.all()
    context = {
        'title' : 'Buku',
        'judul' : 'ini adalah buku',
        'bukutok' : books,
    }
    print(request.user)
    return render(request, 'buku.html', context)

def penerbit(request):
    context = {
        'title' : 'Penerbit',
        'judul' : 'ini adalah penerbit'
    }
    return render(request, 'penerbit.html', context)

def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()

            context = {
                'form' : form,
            }
      
            return render(request, 'tambah-buku.html', context)

    else:
        form = FormBuku()
        context = {
            'form' : form,
        }
    return render(request, 'tambah-buku.html', context)

