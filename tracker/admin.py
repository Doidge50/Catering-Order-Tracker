from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, AuthorAdmin)
admin.site.register(Order, AuthorAdmin)
