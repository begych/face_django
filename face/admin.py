from django.contrib import admin

from .models import *


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "surname")}
    list_display = ('id', 'name', 'surname', 'profession')
    list_display_links = ('id', 'name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ('name', 'surname')


# class Get_inAdmin(admin.ModelAdmin):
#     list_display = ('person_id', 'get_in', 'get_out')
#     list_display_links = ('person_id',)
#     search_fields = ('get_in', 'get_out')
#     list_filter = ('get_in', 'get_out')


admin.site.register(Person, PersonAdmin)
# admin.site.register(Get_in_out, Get_inAdmin)

