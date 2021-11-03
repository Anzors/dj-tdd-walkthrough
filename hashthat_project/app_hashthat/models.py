from django.db import models
from django.forms.fields import CharField

# Create your models here.

class Hash(models.Model):
    text = models.TextField()
    # Note SHA256 give a 64bit hash
    hash = models.CharField(max_length=64)
