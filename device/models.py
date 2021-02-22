from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def mycustomvalidator(value):
    if len(value)>4:
        return True
    else:
        raise ValidationError("must have more than 5 characters")
def val2(value):
    if '0' in value:
        raise ValidationError('Title can to have 0 characters')
    else:
        return True

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,validators=[mycustomvalidator,val2])

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='device/',null=True,blank=True)
    publish_date = models.DateField(auto_now =True)
    type = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'device'


