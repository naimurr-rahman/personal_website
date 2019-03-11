from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^portfolio_details/$', views.portfolio_details,name='portfolio_details'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^services/$', views.services, name='services'),
    url(r'^blog_single/$', views.blog_single, name='blog_single'),
    url(r'^hire_me/$', views.hire_me, name='hire_me'),
]
