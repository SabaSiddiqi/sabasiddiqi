from django.db import models

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


class GraphInput(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    #def __str__(self):
        #template = '{0.x} {0.y}'
        #return template.format(self)
        #return self.x
    #   return '%d %d' % (self.x, self.y)



