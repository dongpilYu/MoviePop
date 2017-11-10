from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'refresh/(?P<predict_id>.+)$', views.refresh)
]