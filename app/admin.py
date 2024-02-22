from django.contrib import admin
from .models import Event, Registration, Person, Team

# Register your models here.

admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Person)
admin.site.register(Team)

