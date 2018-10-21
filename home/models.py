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

class Name(models.Model):
    text = models.CharField(max_length=200)


class GraphInput(models.Model):
    x = models.CharField(max_length=200)
    y = models.CharField(max_length=200)

    def __str__(self):
        return self.x,self.y

