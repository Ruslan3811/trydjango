from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import Http404
# Create your views here.
from .models import Product
from .forms import ProductForm as CreateForm, PureDjangoForm

# def pr(request, my_id):
#     obj = Product.objects.get(id=my_id)
#     context = {
#         'obj': obj
#     }
#     return render(request, "")

def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = CreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj.save()
    context = {
        'form':form
    }
    return render(request, "product_create.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../../")
    context = {
        'obj': obj
    }
    return render(request, "product_delete.html", context)

def product_detail_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    context = {
        'obj': obj
    }
    return render(request, "product_detail.html", context)

def product_create_view(request):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateForm()
    context = {
        'form': form
        }
    return render(request, "product_create.html", context)

def product_list_view(request):
    list_obj = Product.objects.all()
    context = {
        'list_obj': list_obj
    }
    return render(request, "product_list.html", context)

def dynamic_linking_redirecting(request, my_id):
    obj = Product.objects.get(id = my_id)
    context = {
        'obj': obj
    }    
    return render(request, "dynamic_linking_redirecting.html", context)

def dynamic_linking(request):
    query_set = Product.objects.all()
    context = {
        "queryset": query_set
    }
    return render(request, "dynamic_linking.html", context)

def query_set(request):
    query_set = Product.objects.all()
    context = {
        'queryset': query_set
    }
    return render(request, "query_set.html", context)

def deleting_obj(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        redirect("../")
    context = {
        'obj':obj
    }
    return render(request, "deleting_obj.html", context)

def creating_dynamic_url(request, my_id):
    #1-st way:
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    #2-nd way:
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'obj':obj
    }
    return render(request, "dynamic_url.html", context)

def initial_forms(request):
    initial_form = {
        'title': "title of init form",
    }
    # print(dir(PureDjangoForm.objects))
    obj = Product.objects.get(id = 66)
    form = CreateForm(request.POST or None, initial = initial_form, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "initial_forms.html", context)

def pure_django_form(request):
    my_form = PureDjangoForm()
    if request.method == "POST":
        my_form = PureDjangoForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
    context = {
        'form': my_form
    }
    return render(request, "pure_django_form.html", context)

def diff_GET_POST(request):
    if request.method == "POST":
        my_title = request.POST.get('title')
        print(my_title)
    context = {}
    return render(request, "difference_GET_POST.html", context)

def create_form(request):
    # form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.errors
    form = CreateForm()
    context = {
        'form': form
    }
    return render(request, "create_product_form.html", context)

# def create_form(request):
#     if request.method == 'POST':
#         form = CreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('http://127.0.0.1:8000/create_form/')
#     else:
#         form = CreateForm()
#     # form = CreateForm()
#     context = {
#         'form': form
#     }
#     return render(request, "create_product_form.html", context)

def detail_view(request):
    obj = Product.objects.get(id=1)
    context = {'obj':obj}
    return render(request, "detail_products.html", context)

