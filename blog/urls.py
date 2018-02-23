
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.craft_list, name='craft_list'),
    url(r'^vote/(?P<id>\d+)/$',views.craft_vote, name='craft_vote'),

]