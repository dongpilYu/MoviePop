from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'serve/(?P<predict_id>.+)$', views.serve)
]

handler400 = 'blog.views.bad_request'