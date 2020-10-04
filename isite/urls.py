from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from . import views


app_name = 'isite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
