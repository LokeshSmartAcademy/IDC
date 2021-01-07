from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register , name= "register"),
    path('login', views.login, name ="login"),
    path('logout', views.logout, name ="logout"),
    path('otpauth', views.getotp, name= "getotp"),
    path('otpcheck', views.otpcheck, name="otpcheck"),
    path('snippet', views.snippet_detail, name="snippet")
]