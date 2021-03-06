"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myapp import views
from django.contrib.auth import views as auth_views
from myapp import views as accounts_views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^course/(?P<code_name>[-\w]+)/$', views.course, name='course'),
    url(r'^firstprogramming/(?P<code_name>[-\w]+)/$', views.lesson, name='lesson'),
    url(r'^firstprogramming/(?P<code_name>[-\w]+)/(?P<name>[-\w]+)/$', views.learn, name='learn'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^store/$', views.store, name='store'),
    url(r'^navcourse/$', views.navcourse, name='navcourse'),
]
