from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('spblitgid/', include('litgid.urls')),
    path('', include('isite.urls')),
    path('newsletter/', include('newsletter.urls')),

]
