from django.urls import path


from . import views


urlpatterns = [
    path('', views.order_list, name='index'),
    path('create', views.create_order, name='create'),
]