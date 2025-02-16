
from django.urls import path
from make_pages.views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('property-agent/', property_agent, name="property_agent"),
    path('property-list/', property_list, name="property_list"),
    path('property-type/', property_type, name="property_type"),
    path('contact/', contact, name="contact"),
    path('testimonial/', testimonial, name="testimonial"),
    path('error_404/', error_page, name="error_404")
]

