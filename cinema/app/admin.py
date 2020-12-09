from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Movie)
admin.site.register(MovieShow)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(BookingTicket)