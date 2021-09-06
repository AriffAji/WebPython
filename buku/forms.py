from django.forms import ModelForm
from django import forms
from .models import *

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class' : 'form-control',
                'placeholder':'Isi Judul Buku Anda'}),
            'penulis' : forms.TextInput({'class' : 'form-control',
                'placeholder':'Masukkan Nama Penulis'}),
            'penerbit' : forms.TextInput({'class' : 'form-control',
                'placeholder':'Masukkan Nama Penerbit'}),
            'jumlah' : forms.NumberInput({'class' : 'form-control',
                'placeholder':'Masukkan Jumlah Buku yang tersedia'}),
            'kelompok_id' : forms.Select({'class' : 'form-control'}),
        }