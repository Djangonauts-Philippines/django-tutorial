from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    This allows us to add custom fields while keeping all the built-in User functionality.
    """

    # Add custom fields here as needed
    # Example: bio, avatar, phone_number, etc.
    bio = models.TextField(max_length=500, blank=True, help_text="User's biography")
    birth_date = models.DateField(null=True, blank=True, help_text="User's birth date")
    location = models.CharField(max_length=100, blank=True, help_text="User's location")

    class Meta:
        db_table = "auth_user"  # Keep the same table name as Django's default User model

    def __str__(self):
        return self.username
