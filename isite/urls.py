<<<<<<< HEAD
from django.urls import include, path
from . import views


app_name = 'isite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post'),
    
    ]
||||||| empty tree
=======
from django.urls import include, path
from . import views


app_name = 'isite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post'),
    path('<str:slug>/', views.PageDetailView.as_view(), name='page'),
    ]
>>>>>>> 99d275ab85adf490f6b1f3c4f69a21702521e833
