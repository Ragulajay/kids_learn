from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
    path('',views.all_category,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('game/', views.game_view, name='game'),
    path('eng/', views.spl,name='eng'),
    path('mat/', views.mat,name='mat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf import settings
from django.conf.urls.static import static

def static_urlpatterns():
    return static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static_urlpatterns()