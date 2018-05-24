from django.contrib import admin

# Register your models here.
from .models import User,Word


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','nickname','wordbook','email','word_num_today','word_num_remember',
                    'day_signup', 'word_total_remember', 'word_total_plan', 'record']

class WordAdmin(admin.ModelAdmin):
    list_display = ['wordname', 'group', 'soundmark','explanation','demo_1',
                    'demo_1_translate', 'demo_1','demo_1_translate','demo_2','demo_2_translate','demo_3','demo_3_translate']

admin.site.register(User, UserAdmin)
admin.site.register(Word, WordAdmin)