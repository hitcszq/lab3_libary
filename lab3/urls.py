"""lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from lab3app import views
import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','lab3app.views.index'),
    url(r'^search/$','lab3app.views.search'),
    url(r'^search_info/$','lab3app.views.search_info'),
    url(r'delete/$','lab3app.views.delete'),
    url(r'add_book/$','lab3app.views.add_book'),
    url(r'add_author/$','lab3app.views.add_author'),
    url(r'restore/$','lab3app.views.restore'),
    url(r're_load/$','lab3app.views.re_load'),
    url(r'^css/(?P<path>.*)', 'django.views.static.serve',
        {'document_root': settings.CSS_DIR}),
]

