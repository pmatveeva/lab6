from django.conf.urls import url
from . import views
from shop.views import NewView, BasicView, SaleView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/', views.shopping, name='shopping'),
    url(r'^search-new/', NewView.as_view()),
    url(r'^search-basic/', BasicView.as_view()),
    url(r'^search-sale/', SaleView.as_view())
]