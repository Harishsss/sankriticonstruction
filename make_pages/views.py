from django.shortcuts import render,redirect
from make_pages.models import *
from django.db import connection
from django.db.models import Sum
# Create your views here.



def home(request):
    heading="Home"
    status = request.GET.get('status')
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    ph =Heading.objects.filter(status = 2)
    section_one = ph.filter(slug='owl-1')
    clients = ph.filter(slug__startswith='client')
    project_headings = ph.filter(slug='project-heading')
    deliver_projects = ph.exclude(id__in=[69,70])
    about_paragraph =ph.filter(slug='about_paragraph')
    video_paragraph = ph.filter(slug='video')

    category=CategoryVideo.objects.filter(status=2,parent_id=78)

    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    section_image = image_page.filter(parent_id=20)
    projects = Project.objects.filter(status = 2,)
    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    if status == '2':
        projects=projects.filter(constructions_status__in=[2,3])
    if status == '3':
        projects=projects.filter(constructions_status=1)
    projects=projects[:6]
    return render(request, 'constructions/home.html', locals())

    
def about(request):
    heading="About"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    projects = Project.objects.filter(status = 2)
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    about_us = Heading.objects.filter(status = 2,parent__id=19)
    deliver_projects = about_us.exclude(id__in=[69,70])
    about_paragraph =about_us.filter(slug='about_paragraph')
    agent_phs =about_us.filter(slug='agent')
    section_image = image_page.filter(parent_id=24)

    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    return render(request, 'constructions/about.html', locals())

def project(request):
    status = request.GET.get('status')
    load = request.GET.get('load','0')
    heading="Project"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    ph = Heading.objects.filter(status = 2)
    project_headings=ph.filter(slug='project-heading')
    
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    projects = Project.objects.filter(status = 2,)
    section_image = image_page.filter(parent_id=100)
    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    if status == '2':
        projects=projects.filter(constructions_status__in=[2,3])
    if status == '3':
        projects=projects.filter(constructions_status=1)
    return render(request, 'constructions/project.html', locals())

def category(request):
    heading="category"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    projects = Project.objects.filter(status = 2,)
    proposes = image_page.filter(parent_id=89)
    ph = Heading.objects.filter(status = 2)
    our_story=ph.filter(slug='our-story')
    category_one=ph.filter(slug='category-1')
    category_two=ph.filter(slug='category-2')
    category_three=ph.filter(slug='category-3')
    section_image = image_page.filter(parent_id=98)

    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    on_projects = OngoingProject.objects.filter(status=2,parent=None)
    category=CategoryVideo.objects.filter(status=2)
    poojas=category.filter(parent_id=79)
    customers=category.filter(parent_id=86)
    completed_projects=category.filter(parent_id=83)

    
    return render(request, 'constructions/category.html', locals())

def property_type(request):
    heading="Property agent"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    projects = Project.objects.filter(status = 2,)
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    return render(request, 'constructions/property-type.html', locals())


def contact(request):
    heading="Contact"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    section_image = image_page.filter(status = 2,parent_id=32)
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