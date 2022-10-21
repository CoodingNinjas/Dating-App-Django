from django.urls import path
from Boo import views

app_name= 'Boo'

urlpatterns = [
    path('', views.product, name='product'),
    path('learn/', views.learn, name='learn'),
    path('policy/', views.policy, name='policy'),
    path('security/', views.security, name='security'),
    path('guildline/', views.guildline, name='guildline'),
    path('register/', views.register, name='register'),
    path('signin', views.signin, name='signin'),
   
    
   
]