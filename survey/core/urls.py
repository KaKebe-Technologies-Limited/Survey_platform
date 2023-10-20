from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:id>', views.view_item,name='view'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('success/', views.success_page, name='success'),
]