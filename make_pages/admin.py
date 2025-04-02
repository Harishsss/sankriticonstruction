from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Menus)
class MenusAdmin(ImportExportModelAdmin):
    list_display = ['id','name','slug','parent','app_link','icon','menu_order',
                    'server_modified_on', 'status']
    fields = ['name','slug','parent','app_link','icon', 'menu_order', 'status']
    search_fields = ['id','name']
    # list_per_page = 15
    list_filter = ['parent__name']


@admin.register(Heading)
class HeadingAdmin(ImportExportModelAdmin):
    list_display = ['id','name','slug','parent','paragraph','button','btn_link','icon','order',
                    'server_modified_on', 'status']
    fields = ['name','slug','parent','paragraph','image','button','btn_link','icon', 'order', 'status']
    search_fields = ['id','name']
    # list_per_page = 15
    list_filter = ['parent__name']

@admin.register(ImagePage)
class ImagePageAdmin(ImportExportModelAdmin):
    list_display = ['id','name','parent','paragraph','image','order','icon',
                    'server_modified_on', 'status']
    fields = ['name','parent','paragraph','image','icon', 'order', 'status']
    search_fields = ['id','name']
    # list_per_page = 15
    list_filter = ['parent__name']



@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = ['id','name','gmail','subject','phone','message',
                    'server_modified_on', 'status']
    fields = ['name','gmail','subject', 'phone','message','status']
    search_fields = ['id','name']
    # list_per_page = 15

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ['name','constructions_name','rating','price_of_constructions','bed','sqft','bath','image','address','constructions_status','order','server_modified_on', 'status']
    fields = ['name','constructions_name','rating','price_of_constructions','bed','sqft','bath','image','address','constructions_status','order', 'status']
    search_fields = ['name']

@admin.register(OngoingProject)
class OngoingProjectAdmin(ImportExportModelAdmin):
    list_display = ['name','image','parent','order','server_modified_on', 'status']
    fields = ['name','image','parent','order', 'status']
    search_fields = ['parent__name']


@admin.register(CategoryVideo)
class CategoryVideoAdmin(ImportExportModelAdmin):
    list_display = ['name','video','parent','order','server_modified_on', 'status']
    fields = ['name','video','parent','order', 'status']
    search_fields = ['parent__name']

@admin.register(PropertyAgent)
class PropertyAgentAdmin(ImportExportModelAdmin):
    list_display = ['name','designation','link_1','link_2','link_3','image','icon_1','icon_2','icon_3','order','server_modified_on', 'status']
    fields = ['name','designation','link_1','link_2','link_3','image','icon_1','icon_2','icon_3','order','status']
    search_fields = ['name']


@admin.register(StartProject)
class StartProjectAdmin(ImportExportModelAdmin):
    list_display = ['id','name','gmail','phone',
                    'server_modified_on', 'status']
    fields = ['name','gmail', 'phone','status']
    search_fields = ['id','name']
