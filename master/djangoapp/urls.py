from django.urls import path,include
from djangoapp import views

urlpatterns = [
    path('', views.category_form,name='category_insert'), # get and post req. for insert operation
    path('<int:id>/', views.category_form,name='category_update'), # get and post req. for update operation
    path('delete/<int:id>/', views.category_delete,name='category_delete'),
    path('list/', views.category_list,name='category_list'), # get req. to retrieve and display all records
   
    path('product/', views.product_form,name='product_insert'),
    path('product/<int:id>/', views.product_form,name='product_update'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),
    path('product/list/', views.product_list, name='product_list'),
]