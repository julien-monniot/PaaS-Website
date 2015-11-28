# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import WuProfil


class WuInline(admin.StackedInline):
    model = WuProfil
    can_delete = False
    verbose_name_plural = 'WUs'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = [WuInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)