from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class BaseContent(models.Model):
    ACTIVE_CHOICES = ((1, 'Inactive'), (2, 'Active'))
    status = models.PositiveIntegerField(
        choices=ACTIVE_CHOICES, default=2, db_index=True)
    server_created_on = models.DateTimeField(auto_now_add=True)
    server_modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', null=True, blank=True,)
    modified_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', null=True, blank=True,)

class Menus(BaseContent):
    #-------------------#
    # Menus module
    # parent is a foriegn key
    # slug field is used
    #--------------------#
    name = models.CharField(max_length=100)
    group = models.ManyToManyField(Group, blank=True)
    slug = models.SlugField("SEO friendly url, use only aplhabets and hyphen", max_length=60,unique=True)
    parent = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank=True, null=True)
    app_link = models.CharField(max_length=512, blank=True)
    icon = models.CharField(max_length=512, blank=True, null=True)
    menu_order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('menu_order',)
        verbose_name_plural = 'Menus'

    def __str__(self):
        # string method to return name
        hairarchy_name = self.name
        if self.parent:
            hairarchy_name = hairarchy_name +'--'+ self.parent.name
            if self.parent.parent:
                hairarchy_name = hairarchy_name +'--'+ self.parent.parent.name
        return hairarchy_name
    
    def get_sub_menus(self):
        # model method to filter menus based parent id
        return Menus.objects.filter(parent=self,status=2).order_by('menu_order')