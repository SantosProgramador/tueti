from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^list$', views.TuetListAPI.as_view()),
]