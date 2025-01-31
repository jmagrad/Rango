from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin table
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page,PageAdmin)
# Register your models here.
