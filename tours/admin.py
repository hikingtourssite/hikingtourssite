from django.contrib import admin
from .models import Tour, Booking, Review, TourStop

admin.site.register(Booking)
admin.site.register(Review)

class TourStopInline(admin.TabularInline):
    model = TourStop
    extra = 1

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourStopInline]