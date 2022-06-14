from django.urls import path
from . import views

app_name = 'nlp_app'
urlpatterns = [
    path('', views.IndexView, name='home'),
    path('^mock/$', views.NLPView, name='nlp'),
]