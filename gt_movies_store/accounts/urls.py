from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='accounts.signup'),
    path('signin/', views.signin, name='accounts.signin'),
    path('signout/', views.signout, name='accounts.signout'),
    path('orders/', views.orders, name='accounts.orders'),
]