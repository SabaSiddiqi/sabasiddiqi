from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import datetime


from django_mysql.models import ListCharField
# comments
# Create your models here.
# class model_name(models.Model):
#   text=models.Charfield(max_length=25)

# After updating model update database
#   python manage.py makemigrations app_name
# open shell
#   python manage.py shell
#   model_name=Model_name(model_variable=".....")
#   model_name.save()
#   Model_name.objects.all()

class CatIndex(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    link = models.CharField(max_length=500, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        template = '{0.name}'
        return template.format(self)



class GraphInput(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    #def __str__(self):
        #template = '{0.x} {0.y}'
        #return template.format(self)
        #return self.x
    #   return '%d %d' % (self.x, self.y)

from django.db import models
from tinymce import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
