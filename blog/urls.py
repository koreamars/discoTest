
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.craft_list, name='craft_list'),
]