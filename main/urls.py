from django.urls import path
from . import views
from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path(r'^favicon\.ico$', favicon_view),
    path('create', views.create, name='create'),
]
