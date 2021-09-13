from .models import Computer
from django.urls import  reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView, 
                                DetailView, 
                                ListView, 
                                UpdateView, 
                                DeleteView
                                )

from .forms import ComputerModelForm
from django.shortcuts import get_object_or_404
# Create your views here.

class UpdateComputersView(UpdateView):
    template_name = "computer_create.html"
    form_class = ComputerModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Computer, id = id_)

    def form_valid(self, form):
        # print (form.cleaned_data)
        return (super().form_valid(form))
    

class DeleteComputersView(DeleteView):
    template_name = "computer_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Computer, id = id_)

    def get_success_url(self):
        return (reverse('computers:Computer-List'))

class CreateComputersView(CreateView):
    template_name = "computer_create.html"
    form_class = ComputerModelForm
    queryset = Computer.objects.all()

    def form_valid(self, form):
        # print (form.cleaned_data)
        return (super().form_valid(form))

class ListComputersView(ListView):
    template_name = "computer_list.html"
    queryset = Computer.objects.all()

class DetailComputersView(DetailView):
    template_name = "computer_detail.html"
    queryset = Computer.objects.all()
    #for second way:
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Computer, id = id_)


# def ComputerDetail(request, my_id):
#     obj = get_object_or_404(Computer ,id = my_id)
#     context = {
#         'obj':obj
#     }
#     return render(request, "computer_detail.html", context)