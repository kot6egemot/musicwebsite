from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import auth_login

from .views import logout_view,login_view,register_view



app_name = 'users'

urlpatterns = [
    path('login/', login_view, name = 'login_view'),
    path('logout/', logout_view, name = 'logout_view'),
    path('register/', register_view, name = 'register_view'),
]
