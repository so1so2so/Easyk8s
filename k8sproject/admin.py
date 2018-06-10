# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from k8sproject import models


class My_All_api_for_k8s(admin.ModelAdmin):
    list_display = ('id', 'api_name', 'menu_name')
    list_filter = ('menu_name',)
    # filter_horizontal = ('menu_name',)


class MY_Menu(admin.ModelAdmin):
    list_display = ('name', 'url_type', 'url_name')
    list_filter = ('name',)


admin.site.register(models.Menu, MY_Menu)
admin.site.register(models.All_api_for_k8s, My_All_api_for_k8s)
admin.site.register(models.Show_content)
admin.site.register(models.Role)
admin.site.register(models.UserProfile)
admin.site.register(models.namespace)
admin.site.register(models.result)
