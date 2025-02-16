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