
from django.urls import path
from make_pages.views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('project/', project, name="project"),
    path('residential/', residential, name="residential"),
    path('commercial/', commercial, name="commercial"),
    path('interiors/', interiors, name="interiors"),
    path('contact/', contact, name="contact"),

]

