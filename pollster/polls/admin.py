from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollster admin"
admin.site.site_title = "Pollster Admmin Area"
admin.site.index_title = "Welcome to pollster admin area"


# admin.site.register(Question)
# admin.site.register(Choice)
# TabularInline - To have the choices within the question's admin field

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

