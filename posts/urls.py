from django.conf.urls import url

from . import views


app_name = 'posts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^(?P<post_id>[0-9]+)/add_comment/', views.add_comment, name='add_comment'),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.delete_post, name='delete'),
    url(r'^(?P<post_id>[0-9]+)/post-form/$', views.post_form, name='post-form'),
    url(r'^(?P<post_id>[0-9]+)/update/$', views.update_post, name='update'),
    url(r'^add_post/$', views.add_post, name='add_post'),

]
