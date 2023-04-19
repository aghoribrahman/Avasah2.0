from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'), 
    path('blog/<int:id>',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'), 
    path('portfolio/',views.portfolio, name='portfolio'),
    path('service/',views.service, name='service'), 
    path('single/<int:id>',views.single, name='single'),
    path('team/',views.team, name='team'), 
    path('query/',views.query, name='query'), 
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
