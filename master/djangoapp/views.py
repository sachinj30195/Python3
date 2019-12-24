from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from .models import Category,Product
from .forms import CategoryForm,ProductForm

def category_list(request):

    context = Category.objects.all()
    paginator = Paginator(context,10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'category/category_list.html', {'category_list': posts, 'page': page})
def category_form(request, id = None):

    if request.method == "GET":
        if id == None:
            form = CategoryForm()
        else:
            cat = get_object_or_404(Category, id = id)
            # cat = Category.objects.get(id=id)
            form = CategoryForm(instance = cat)
        return render(request, "category/category_form.html", {'form': form})
    else:
        if id == None:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'created succesfully')
        else:
            cat = Category.objects.get(id=id)
            form = CategoryForm(request.POST,instance= cat)
            if form.is_valid():
                form.save()
                messages.success(request,'updated succesfully')
        return redirect('/category/list')

def category_delete(request,id):
    # cat = Category.objects.get(id=id)
    cat = get_object_or_404(Category,id=id)
    cat.delete()
    messages.success(request,'deleted succesfully')
    return redirect('/category/list')

def product_list(request):

    context = Product.objects.all()
    paginator = Paginator(context,10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'product/product_list.html', {'product_list': posts,'page': page})
def product_form(request, id = None):

    if request.method == "GET":
        if id == None:
            form = ProductForm()
        else:
            pro=get_object_or_404(Product,id=id)

            form = ProductForm(instance=pro)
        return render(request, "product/product_form.html", {'form': form})
    else:
        if id == None:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'created succesfully')
        else:
            pro = Product.objects.get(id=id)
            form = ProductForm(request.POST,instance= pro)
            if form.is_valid():
                form.save()
                messages.success(request, 'updated succesfully')
        return redirect('/category/product/list/')
        
def product_delete(request, id):
    # cat = Category.objects.get(id=id)
    pro=get_object_or_404(Product, id=id)
    pro.delete()
    messages.success(request, 'deleted succesfully')
    return redirect('/category/product/list/')




