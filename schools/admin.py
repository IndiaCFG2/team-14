from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Boards)
admin.site.register(models.Schools)
