"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, contact_view, about_view, social_view

urlpatterns = [
    path('computers/', include('computers.urls')),
    path('blog/', include('blog.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('social/', social_view, name='social'),
    path('about/<int:my_id>/', about_view),
    path('home/<int:my_id>/', home_view, name='product-detail'),
    # path('detail/', detail_view, name='detail'),
    # path('create_form/', create_form, name='form'),
    # path('diff_GET_POST/', diff_GET_POST),
    # path('pure_django_form/', pure_django_form),
    # path('initial_forms/', initial_forms),
    # path('dynamic_url/<int:my_id>/', creating_dynamic_url),
    # path('dynamic_url/<int:my_id>/delete/', deleting_obj),
    # path('deleting_obj/<int:my_id>/delete/', deleting_obj),
    # path('query_set/', query_set),
    # path('dynamic_linking/', dynamic_linking, name='dynamic'),
    # path('dynamic_/<int:my_id>/', dynamic_linking_redirecting, name='dynamic_redirecting'),
    # path('home/', home_view),
]
