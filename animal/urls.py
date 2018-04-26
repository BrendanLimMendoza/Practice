from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view.as_view(), name="index"),
    url(r'^create/$', views.CreateAnimalView.as_view(), name="create"),


  #  url(r'^(?P<pk>[0-9]+)/$', views.detail_view.as_view(), name='detail'),

  #  url(r'animal/add/$', views.create_animal.as_view(), name='create-animal'),

    #edit animal url
    url(r'animal/(?P<pk>[0-9]+)/$', views.UpdateAnimal.as_view(), name='update-animal'),

    url(r'animal/(?P<pk>[0-9]+)/delete/$', views.DeleteAnimal.as_view(), name='delete-animal'),
]

