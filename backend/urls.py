from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.admin_login,name='backend.login'),
    path('home/',views.home_page,name="backend.home"),
    path('logout/',views.admin_logout,name="backend.logout")
]
