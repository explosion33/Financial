from django.contrib import admin
from django.db.models import Model
import inspect
from . import models

# Register your models here.

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj) and issubclass(obj, Model):
        admin.site.register(obj)


 