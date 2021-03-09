from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'Polls Center'
admin.site.index_title = 'Pollster'
admin.site.site_title = 'Your Own Polls'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date Published", {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)