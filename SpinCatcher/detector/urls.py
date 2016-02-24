from django.conf.urls import url

from . import views

app_name = 'detector'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^', views.SearchView.as_view(), name='search'),
]