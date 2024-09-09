from django.urls import path 
from . import views 



urlpatterns = [
    path('accounts/login/',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register_view,name='register'),
    path('profile',views.profile,name='profile'),
    path('passwordChange',views.password_change,name='passwordChange'),
    path('order',views.order,name='order'),
    ]