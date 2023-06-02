from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('maths',views.maths,name='maths'),

]