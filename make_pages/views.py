from django.shortcuts import render
from make_pages.models import *

# Create your views here.


def home(request):
    heading="Home"
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    print(menus)
    return render(request, 'constructions/home.html', locals())

def about(request):
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    heading="About"
    return render(request, 'constructions/about.html', locals())

def property_agent(request):
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    heading="Property agent"
    return render(request, 'constructions/property-agent.html', locals())

def property_list(request):
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    heading="Property agent"
    return render(request, 'constructions/property-list.html', locals())

def property_type(request):
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    heading="Property agent"
    return render(request, 'constructions/property-type.html', locals())


def contact(request):
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    heading="Contact"
    return render(request, 'constructions/contact.html', locals())


def testimonial(request):
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    heading="Testimonial"
    return render(request, 'constructions/testimonial.html', locals())

def error_page(request):
    heading="404"
    menus = Menus.objects.filter(status = 2, parent=None).order_by("menu_order")
    return render(request, 'constructions/404.html', locals())