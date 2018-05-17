from django.contrib import admin

# Register your models here.
from .models import User,Word


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password']

class WordAdmin(admin.ModelAdmin):
    list_display = ['wordname', 'group', 'soundmark','explanation']

admin.site.register(User, UserAdmin)
admin.site.register(Word, WordAdmin)