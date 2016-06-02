from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date info', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
