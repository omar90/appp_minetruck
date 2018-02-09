from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^filter/', views.contact, name='contact'),]

# Create your views here.
