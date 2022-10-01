from django.contrib import admin
from .models import friend, message
# Register your models here.
admin.site.register([friend,message])
