from django.contrib import admin

# Register your models here.
from .models import boardmodul, comment
admin.site.register(boardmodul)
admin.site.register(comment)
