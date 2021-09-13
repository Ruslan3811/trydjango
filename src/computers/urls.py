from django.urls import path
from .views import ListComputersView, DetailComputersView, CreateComputersView, UpdateComputersView, DeleteComputersView

app_name='computers'

urlpatterns = [   
    #first way:
    # path('<int:pk>/', DetailComputersView.as_view(), name='computer-detail'),    
    #second way
    path('<int:id>/', DetailComputersView.as_view(), name='computer-detail'),
    path('create/', CreateComputersView.as_view(), name='computer-create'),
    path('<int:id>/update/', UpdateComputersView.as_view(), name='computer-update'),
    path('<int:id>/delete/', DeleteComputersView.as_view(), name='computer-delete'),    
    path('', ListComputersView.as_view(), name='Computer-List')
]