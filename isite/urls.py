from django.urls import include, path
from . import views


app_name = 'isite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post'),
    
    ]
