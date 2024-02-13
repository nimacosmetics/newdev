from django.urls import path

from .import views 

urlpatterns = [
    path('', views.hompage, name=""),
    path('login', views.login_view, name="login"),
    path('dashbord', views.dashbord, name="dashbord"),
    path('register', views.register, name="register"),
    path("logout",views.logout_view, name="logout")
]