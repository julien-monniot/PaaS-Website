from django.contrib import admin
from .models import Travel, Participate, Stage


class ParticipateInline(admin.TabularInline):
    model = Participate
    extra = 1
    fields = ['person', 'motivation']


class StageInLine(admin.StackedInline):
    model = Stage
    extra = 1
    fields = ['title', 'point_of_departure', 'point_of_arrival', 'description', 'duration']



class TravelCustomAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Objet du voyage', {'fields': ['title', 'author', 'created_date', 'description', 'budget']}),
        ('Dates', {'fields': ['starting_date', 'ending_date']}),
        ('Image', {'fields': ['image']})
    ]
    inlines = [ParticipateInline, StageInLine]

admin.site.register(Travel, TravelCustomAdmin)