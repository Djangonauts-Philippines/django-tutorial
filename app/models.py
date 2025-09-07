from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


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


class Post(models.Model):
    """
    Post model.
    """

    title = models.CharField(max_length=200, help_text="Post title")
    slug = models.SlugField(max_length=200, unique=True, help_text="URL-friendly version of title")
    content = models.TextField(help_text="Post content")
    excerpt = models.TextField(max_length=300, blank=True, help_text="Short excerpt for preview")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True, help_text="When the post was published")
    is_published = models.BooleanField(default=False, help_text="Whether the post is published")

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("app:post_detail", kwargs={"slug": self.slug})
