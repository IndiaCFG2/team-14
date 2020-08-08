from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Tech_level)
admin.site.register(models.Week)
admin.site.register(models.DName)
admin.site.register(models.Subject)
admin.site.register(models.Grade)
admin.site.register(models.Course)

