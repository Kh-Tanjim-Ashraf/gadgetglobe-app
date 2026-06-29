from django.db import models
from django.contrib.auth.models import User
from shared.models import TimestampMixins



class UserProfile(TimestampMixins):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="user/")

    def __str__(self):
        return self.user_id.username



class Phone(TimestampMixins):
    user_profile_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=14)

    def __str__(self):
            return f"{self.phone}---{self.user_profile_id}"



class Address(TimestampMixins):
    user_profile_id = models.ManyToManyField(UserProfile, related_name="addresses")
    address_line = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.address_line}, {self.street}, {self.city}, {self.postal_code}"