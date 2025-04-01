
from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', contact_view, name='contact_form'),
    path('our_goals/', views.our_goals, name='our_goals'),
    path('programs/', views.programs, name='programs'),
]