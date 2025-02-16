from django.template.defaulttags import register
from make_pages.models import *
from datetime import datetime ,timedelta,date
today = datetime.today()

# @register.simple_tag # This allows access to context
# def get_menu_list():

#     # Example: Customize menu based on authentication

#     print(menus)
#     return menus



# @register.simple_tag
# def get_menu_list():
#     """
#     Return a list of menus.
#     """
#     # group =request.user.groups.all()[0].id
#     # user_mission_list=request.session.get('user_mission_list')
#     menus = []
#     menus = Menus.objects.filter(status = 2, parent_id=1).order_by("menu_order")
#     # if (not request.user.is_superuser) and (not (5 in user_mission_list and 2 in user_mission_list)):
#     #     if 5 in user_mission_list:
#     #         menus = menus.exclude(id=18).order_by("menu_order")
#     #     elif 2 in user_mission_list:
#     #         menus = menus.exclude(id=1).order_by("menu_order")
#     return menus

# @register.simple_tag
# def get_sub_menus(request):
#     group =request.user.groups.all()[0].id
#     application_type_id=request.session.get('application_type_id')
#     if application_type_id == 510:
#         menus = Menus.objects.filter(active = 2,group=group).exclude(id=18).order_by("menu_order")
#     elif application_type_id == 511:
#         menus = Menus.objects.filter(active = 2,group=group).exclude(id=1).order_by("menu_order")
#     else:
#     return Menus.objects.filter(parent=self).order_by('menu_order')

