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

    # class Meta:
    #     abstract = True


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
        return Menus.objects.filter(parent=self,status=2).exclude(parent__id__in=[1,12,16]).order_by('menu_order')
    

class Heading(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    parent = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank=True, null=True)
    slug = models.SlugField("SEO friendly url, use only aplhabets and hyphen", max_length=60,unique=True)
    paragraph=models.TextField(blank=True, null=True)
    button = models.CharField(max_length=512, blank=True)
    btn_link = models.CharField(max_length=512, blank=True)
    icon = models.CharField(max_length=512, blank=True, null=True)
    image = models.ImageField(
        upload_to='client/%y/%m/%d/', blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Heading and Paragraph"

    def __str__(self):
        return self.name
    
class ImagePage(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    icon = models.CharField(max_length=100,blank=True, null=True)
    parent = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank=True, null=True)
    paragraph=models.TextField(blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)
    image = models.FileField(
        upload_to='section/%y/%m/%d/', blank=True, null=True)
    def __str__(self):
        return self.name


    

class ContactUs(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    gmail = models.CharField(max_length=100,blank=True, null=True)
    subject = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)
    message=models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact US"

    def __str__(self):
        return self.name

class Project(BaseContent):
    ACTIVE_CHOICES = ((1, 'Ongoing'), (2, 'Completed'), (3, 'Happy Customer'))

    name = models.CharField(max_length=100,blank=True, null=True)
    constructions_name = models.CharField(max_length=100,blank=True, null=True)
    rating = models.FloatField(blank=True,null=True)
    price_of_constructions = models.BigIntegerField(blank=True,null=True)
    bed = models.PositiveIntegerField(blank=True, null=True)
    sqft = models.PositiveIntegerField(blank=True, null=True)
    bath = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='project/%y/%m/%d/', blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    constructions_status = models.PositiveIntegerField(choices=ACTIVE_CHOICES, default=1)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class OngoingProject(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='project/%y/%m/%d/', blank=True, null=True)
    parent = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_on_going(self):
        # model method to filter menus based parent id
        return OngoingProject.objects.filter(parent=self,status=2)

class CategoryVideo(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    video = models.URLField(max_length=1010, blank=True, null=True)
    parent = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    
    

    class Meta:
        verbose_name_plural = "Category Video"


class PropertyAgent(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    link_1 = models.CharField(max_length=512,blank=True, null=True)
    link_2 = models.CharField(max_length=512,blank=True, null=True)
    link_3 = models.CharField(max_length=512,blank=True, null=True)
    image = models.FileField(upload_to='section/%y/%m/%d/', blank=True, null=True)
    icon_1 = models.CharField(max_length=100,blank=True, null=True)
    icon_2 = models.CharField(max_length=100,blank=True, null=True)
    icon_3 = models.CharField(max_length=100,blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name


class StartProject(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    gmail = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return self.name
    


class Career(BaseContent):
    name = models.CharField(max_length=100,blank=True, null=True)
    gmail = models.CharField(max_length=100,blank=True, null=True)
    role = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)
    experience = models.CharField(max_length=100,blank=True, null=True)
    cv = models.FileField(
        upload_to='cv/%y/%m/%d/', blank=True, null=True)
    message=models.TextField(blank=True, null=True)

  

    def __str__(self):
        return self.name