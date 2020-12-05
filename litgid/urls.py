from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views


app_name = 'litgid'
urlpatterns = [
    path('', views.test, name='index'),
    path('newsletter/', include('newsletter.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
