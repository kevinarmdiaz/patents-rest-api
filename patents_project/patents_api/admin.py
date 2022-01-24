from django.contrib import admin

# Register your models here.
from patents_api import models

admin.site.register(models.UserProfile)