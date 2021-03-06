from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<pk>\d+)/', views.mineral_detail, name='detail')
]
urlpatterns += staticfiles_urlpatterns()
