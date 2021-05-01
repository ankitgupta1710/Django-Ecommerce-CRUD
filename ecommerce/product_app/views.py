from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import *

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductCreate(CreateView):
    model = Product
    # fields = ['code', 'name', 'description','price', 'photo', 'manufacturer', 'offers', 'availablity', 'category']
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

    

class ProductUpdate(UpdateView):
    model = Product
    #fields = ['code', 'name', 'description','price', 'photo', 'manufacturer', 'offers', 'availablity', 'category']
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    
