from django.conf.urls import url 
from crud_app import views 
 
urlpatterns = [ 
    url(r'^api/tutorials/$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)/$', views.tutorial_detail),
    url(r'^api/tutorials/published/$', views.tutorial_list_published),

    url(r'^api/tutorials/(?P<title>\w{0,50})/$', views.tutorial_detail_title),

]