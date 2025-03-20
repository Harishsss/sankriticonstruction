from django.shortcuts import render,redirect
from make_pages.models import *
from django.db import connection
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
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
    section_one = ph.filter(slug='owl-1').order_by('order')
    clients = ph.filter(slug__startswith='client').order_by('order')
    project_headings = ph.filter(slug='project-heading').order_by('order')
    deliver_projects = ph.exclude(id__in=[69,70]).order_by('order')
    about_paragraph =ph.filter(slug='about_paragraph').order_by('order')
    video_paragraph = ph.filter(slug='video').order_by('order')

    category=CategoryVideo.objects.filter(status=2,parent_id=78)

    about_us = Heading.objects.filter(status = 2,parent__id=19).order_by('order')
    deliver_projects = about_us.exclude(id__in=[69,70]).order_by('order')
    about_paragraph =about_us.filter(slug='about_paragraph').order_by('order')
    agent_phs =about_us.filter(slug='agent').order_by('order')
    property_agents=PropertyAgent.objects.filter(status=2).order_by('order')

    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67).order_by('order')
    section_image = image_page.filter(parent_id=20).order_by('order')
    why_choose = image_page.filter(parent_id=106).order_by('order')
    why_choose_ph=about_us.filter(slug='commercial-1')
    
    projects = Project.objects.filter(status = 2,)
    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    if status == '2':
        projects=projects.filter(constructions_status__in=[2,3]).order_by('order')
    if status == '3':
        projects=projects.filter(constructions_status=1).order_by('order')
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
    logos = image_page.filter(parent_id=67).order_by('order')
    about_us = Heading.objects.filter(status = 2,parent__id=19).order_by('order')
    deliver_projects = about_us.exclude(id__in=[69,70])
    about_paragraph =about_us.filter(slug='about_paragraph')
    agent_phs =about_us.filter(slug='agent').order_by('order')
    section_image = image_page.filter(parent_id=24).order_by('order')
    property_agents=PropertyAgent.objects.filter(status=2).order_by('order')

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
    logos = image_page.filter(parent_id=67).order_by('order')
    projects = Project.objects.filter(status = 2,).order_by('order')
    section_image = image_page.filter(parent_id=100).order_by('order')
    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    if status == '2':
        projects=projects.filter(constructions_status__in=[2,3]).order_by('order')
    if status == '3':
        projects=projects.filter(constructions_status=1).order_by('order')
    return render(request, 'constructions/project.html', locals())

def residential(request):
    heading="residential"
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

    
    return render(request, 'constructions/residential.html', locals())

def commercial(request):
    heading="commercial"
    status = request.GET.get('status')

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
    our_story=ph.filter(slug='our-services').order_by('order')
    category_one=ph.filter(slug='category-1').order_by('order')
    category_two=ph.filter(slug='category-2').order_by('order')
    category_three=ph.filter(slug='category-3').order_by('order')
    section_image = image_page.filter(parent_id=98).order_by('order')
    our_process_cards = image_page.filter(parent_id=116).order_by('order')
    associates_logo =image_page.filter(parent_id=128).order_by('order')

    about_us = Heading.objects.filter(status = 2,parent__id=19)
    deliver_projects = about_us.exclude(id__in=[69,70])
    about_paragraph =about_us.filter(slug='about_paragraph').order_by('order')
    agent_phs =about_us.filter(slug='agent').order_by('order')
    why_choose = image_page.filter(parent_id=106).order_by('order')
    why_choose_ph=ph.filter(slug='commercial-1').order_by('order')
    our_process =ph.filter(slug='our-process').order_by('order')
    associates =ph.filter(slug='associate').order_by('order')
    
    agents = ph.filter(slug='agents').order_by('order')
    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    on_projects = OngoingProject.objects.filter(status=2,parent=None)
    category=CategoryVideo.objects.filter(status=2)
    commercial_videos=category.filter(parent_id=122).order_by('order')

    if status == '2':
        projects=projects.filter(constructions_status__in=[2,3]).order_by('order')
    if status == '3':
        projects=projects.filter(constructions_status=1).order_by('order')
    projects=projects[:6]
    return render(request, 'constructions/commercial.html', locals())

def interiors(request):
    heading="interiors"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67)
    projects = Project.objects.filter(status = 2,).order_by('order')
    proposes = image_page.filter(parent_id=89).order_by('order')
    ph = Heading.objects.filter(status = 2)
    our_story=ph.filter(slug='our-story').order_by('order')
    category_one=ph.filter(slug='category-1').order_by('order')
    category_two=ph.filter(slug='category-2').order_by('order')
    category_three=ph.filter(slug='category-3').order_by('order')
    section_image = image_page.filter(parent_id=98).order_by('order')

    increment_counts = [projects.filter(constructions_status__in=[2,3]).count(),projects.filter(constructions_status=3).count(),projects.aggregate(Sum('sqft')).get('sqft__sum')]
    increments=[]
    for  i,j in zip(image_page.filter(status = 2,parent_id=60),increment_counts):
        increments.append({'name':i.name,'icon':i.icon,'count':j})
    on_projects = OngoingProject.objects.filter(status=2,parent=None)
    category=CategoryVideo.objects.filter(status=2)
    poojas=category.filter(parent_id=79).order_by('order')
    customers=category.filter(parent_id=86).order_by('order')
    completed_projects=category.filter(parent_id=83).order_by('order')
    return render(request, 'constructions/interiors.html', locals())


def send_test_email(gmail_id,subject, message):
    # import ipdb; ipdb.set_trace();
    from_email = settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else settings.EMAIL_HOST_USER
    recipient_list = [gmail_id]

    result = send_mail(subject, message, from_email, recipient_list, fail_silently=False)


def contact(request):
    heading="Contact"
    header_list = Menus.objects.filter(status = 2,)
    header=header_list.filter( parent=None).exclude(id__in=[1,12,16]).order_by("menu_order")
    icon=header_list.filter(parent_id=12).order_by("menu_order")
    menu=header_list.filter(parent_id=1).order_by("menu_order")
    map=header_list.filter(id=16).order_by("menu_order")
    image_page=ImagePage.objects.filter(status = 2)
    logos = image_page.filter(parent_id=67).order_by('order')
    section_image = image_page.filter(status = 2,parent_id=32).order_by('order')
    section_one = Heading.objects.filter(status = 2,parent_id=26)

    if request.method == 'POST':
        name=request.POST.get('name'),
        gmail_id=request.POST.get('email'),
        subject=request.POST.get('subject'),
        message=request.POST.get('message'),
        contact_obj =ContactUs.objects.create(
        name=name,
        gmail=gmail_id,
        subject=subject,
        message=message,
        phone=request.POST.get('phone')
        )
        contact_obj.save()
        # send_test_email(gmail_id,subject,message)
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