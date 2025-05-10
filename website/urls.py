
from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', contact_view, name='contact_form'),
    path('our_goals/', views.our_goals, name='our_goals'),
    path('course/', views.course, name='course'),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

