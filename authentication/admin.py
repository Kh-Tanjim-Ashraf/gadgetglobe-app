from django.contrib import admin
from authentication.models import UserProfile, Phone, Address



admin.site.register(UserProfile)
admin.site.register(Phone)
admin.site.register(Address)