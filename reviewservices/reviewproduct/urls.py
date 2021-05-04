from django.urls import path 
from . import views
urlpatterns =[
path('', views.home, name='shuelectronics-home'),
path('about/', views.about, name='shuelectronics-about'),
path('contact/', views.contact, name='shuelectronics-contact'),
path('product/', views.product, name='shuelectronics-product'),

]

