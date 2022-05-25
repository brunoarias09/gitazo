
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from appCoder.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso/', curso),
    path('appCoder/',include('appCoder.urls')),
]
