from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import GraphInput,CatIndex

# Register your models here.
admin.site.register(GraphInput)

admin.site.register(CatIndex, MPTTModelAdmin)

from . import models
admin.site.register(models.Post)
