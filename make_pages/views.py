from django.shortcuts import render,redirect
from make_pages.models import *

# Create your views here.


def home(request):
    heading="Home"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    section_one = Heading.objects.filter(status = 2,slug='owl-1')
    clients = Heading.objects.filter(status = 2,slug__startswith='client')
    project_headings = Heading.objects.filter(status = 2,slug='project-heading')
    section_image = ImagePage.objects.filter(status = 2,parent_id=20)
    projects = Project.objects.filter(status = 2,)
    return render(request, 'constructions/home.html', locals())

    
def about(request):
    heading="About"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")

    return render(request, 'constructions/about.html', locals())

def project(request):
    heading="Project"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    projects = Project.objects.filter(status = 2,)

    return render(request, 'constructions/project.html', locals())

def property_list(request):
    heading="Property agent"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")

    return render(request, 'constructions/property-list.html', locals())

def property_type(request):
    heading="Property agent"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")

    return render(request, 'constructions/property-type.html', locals())


def contact(request):
    heading="Contact"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    section_image = ImagePage.objects.filter(status = 2,parent_id=32)
    section_one = Heading.objects.filter(status = 2,parent_id=26)

    if request.method == 'POST':
        contact_obj =ContactUs.objects.create(name=request.POST.get('name'),
        gmail=request.POST.get('email'),subject=request.POST.get('subject'),
        message=request.POST.get('message'),phone=request.POST.get('phone'))
        contact_obj.save()
        return redirect('/contact/')
    return render(request, 'constructions/contact.html', locals())


def testimonial(request):
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")

    heading="Testimonial"
    return render(request, 'constructions/testimonial.html', locals())

def error_page(request):
    heading="404"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")

    return render(request, 'constructions/404.html', locals())