from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "country", "owner", "start_date", "end_date", "is_archived")
    list_filter = ("is_archived", "travel_style", "country")
    search_fields = ("title", "destination", "owner__username")