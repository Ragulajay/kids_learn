
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

def static_urlpatterns():
    return static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static_urlpatterns()
