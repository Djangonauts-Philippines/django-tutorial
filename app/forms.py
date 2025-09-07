from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for creating and editing posts.
    """

    class Meta:
        model = Post
        fields = ["title", "slug", "content", "excerpt", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}),
            "slug": forms.TextInput(attrs={"class": "form-control", "placeholder": "url-friendly-slug"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 10, "placeholder": "Write your post content here..."}
            ),
            "excerpt": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Optional: Write a short excerpt for preview...",
                }
            ),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "Post Title",
            "slug": "URL Slug",
            "content": "Content",
            "excerpt": "Excerpt (Optional)",
            "is_published": "Publish immediately",
        }
        help_texts = {
            "slug": "URL-friendly version of the title (lowercase, no spaces, use hyphens)",
            "excerpt": "A short preview of your post (optional)",
            "is_published": "Check this to publish the post immediately",
        }
