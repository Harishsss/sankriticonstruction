
from django.urls import path
from make_pages.views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('project/', project, name="project"),
    path('category/', category, name="category"),
    path('property-type/', property_type, name="property_type"),
    path('contact/', contact, name="contact"),
    path('testimonial/', testimonial, name="testimonial"),
    path('error_404/', error_page, name="error_404")
]

