from django.db import models
from jsonfield import JSONField
# Create your models here.

class FormSchema(models.Model):
    title = models.CharField(max_length=100)
    schema = JSONField()

