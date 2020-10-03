from django.urls import include, path
from . import views


app_name = 'isite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post'),
    ]
