from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('admin/', admin.site.urls),
    url(r'^basic_app/',include('basic_app.urls')),
]
