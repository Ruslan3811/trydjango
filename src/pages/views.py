from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home_view(request, *args, **kwargs):
#     print(request.user)
#     return HttpResponse("<h1>Hello World</h1>")

def home_view(request, *args, **kwargs):
    my_context = {
        "my_text": "It's our text, we check passing variables to context",
        "my_name": "My name is Ruslan",
        "My_age": "My age is" + " 22",
        "My_list": [22, 63, 1, "abc"]
    }
    return render(request, 'home_view.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact_view.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about_view.html', {})

def social_view(request, *args, **kwargs):
    return render(request, 'social_view.html', {})
