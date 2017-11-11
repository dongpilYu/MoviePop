from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'refresh/(?P<predict_id>.+)$', views.refresh),
    url(r'^admin/',include(admin.site.urls))
]