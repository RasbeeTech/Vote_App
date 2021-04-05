from django.contrib import admin

from .models import Question, Choice


# admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    """fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]"""
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # Add choices to the Question section
    inlines = [ChoiceInline]
    # sets column titles for admin change list [Change list]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # add filter sidebar [Change list]
    list_filter = ['pub_date']
    # add searching capabilities [Change list]
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
