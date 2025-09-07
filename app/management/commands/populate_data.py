from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime, timedelta
import random

from app.models import Post

User = get_user_model()


class Command(BaseCommand):
    help = "Populate the database with sample users and posts"

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=10, help="Number of users to create (default: 10)")
        parser.add_argument("--posts", type=int, default=50, help="Number of posts to create (default: 50)")
        parser.add_argument("--clear", action="store_true", help="Clear existing users and posts before populating")

    def handle(self, *args, **options):
        users_count = options["users"]
        posts_count = options["posts"]
        clear_existing = options["clear"]

        if clear_existing:
            self.stdout.write("Clearing existing data...")
            Post.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()
            self.stdout.write(self.style.SUCCESS("Existing data cleared."))

        # Create users
        self.stdout.write(f"Creating {users_count} users...")
        users = self.create_users(users_count)
        self.stdout.write(self.style.SUCCESS(f"Successfully created {len(users)} users."))

        # Create posts
        self.stdout.write(f"Creating {posts_count} posts...")
        posts = self.create_posts(posts_count, users)
        self.stdout.write(self.style.SUCCESS(f"Successfully created {len(posts)} posts."))

        self.stdout.write(self.style.SUCCESS("Database population completed!"))

    def create_users(self, count):
        """Create sample users with realistic data."""
        users = []

        # Sample user data
        user_data = [
            {
                "username": "alice_writer",
                "email": "alice@example.com",
                "first_name": "Alice",
                "last_name": "Johnson",
                "bio": "Passionate writer and blogger with 5+ years of experience in tech writing.",
                "location": "San Francisco, CA",
            },
            {
                "username": "bob_developer",
                "email": "bob@example.com",
                "first_name": "Bob",
                "last_name": "Smith",
                "bio": "Full-stack developer who loves sharing knowledge about web development.",
                "location": "New York, NY",
            },
            {
                "username": "charlie_designer",
                "email": "charlie@example.com",
                "first_name": "Charlie",
                "last_name": "Brown",
                "bio": "UI/UX designer with a passion for creating beautiful and functional interfaces.",
                "location": "Austin, TX",
            },
            {
                "username": "diana_analyst",
                "email": "diana@example.com",
                "first_name": "Diana",
                "last_name": "Wilson",
                "bio": "Data analyst and business intelligence expert.",
                "location": "Seattle, WA",
            },
            {
                "username": "eve_marketer",
                "email": "eve@example.com",
                "first_name": "Eve",
                "last_name": "Davis",
                "bio": "Digital marketing specialist focused on growth and engagement.",
                "location": "Los Angeles, CA",
            },
        ]

        # Create predefined users
        for data in user_data:
            if not User.objects.filter(username=data["username"]).exists():
                user = User.objects.create_user(
                    username=data["username"],
                    email=data["email"],
                    password="password123",  # Default password for demo
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    bio=data["bio"],
                    location=data["location"],
                )
                users.append(user)

        # Create additional random users if needed
        remaining_count = count - len(users)
        for i in range(remaining_count):
            username = f"user_{i + 1}"
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=f"{username}@example.com",
                    password="password123",
                    first_name=f"User{i + 1}",
                    last_name="Demo",
                    bio=f"This is a demo user created for testing purposes.",
                    location=random.choice(
                        ["Chicago, IL", "Denver, CO", "Miami, FL", "Portland, OR", "Boston, MA", "Phoenix, AZ"]
                    ),
                )
                users.append(user)

        return users

    def create_posts(self, count, users):
        """Create sample posts with realistic content."""
        posts = []

        # Sample post data
        post_templates = [
            {
                "title": "Getting Started with Django: A Beginner's Guide",
                "content": """Django is a powerful web framework for Python that makes it easy to build web applications quickly. In this comprehensive guide, we'll cover the basics of Django development.

## What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the "batteries included" philosophy, providing many features out of the box.

## Key Features

- **Admin Interface**: Django comes with a built-in admin interface that's automatically generated from your models.
- **ORM**: Django's Object-Relational Mapping allows you to interact with your database using Python code.
- **URL Routing**: Clean URL patterns that map to your views.
- **Template System**: A powerful templating engine for rendering HTML.

## Getting Started

To get started with Django, you'll need to:

1. Install Django using pip
2. Create a new Django project
3. Set up your database
4. Create your first app

Let's dive into each step in detail...""",
                "excerpt": "Learn the fundamentals of Django web development with this comprehensive beginner's guide.",
            },
            {
                "title": "Python Best Practices for Clean Code",
                "content": """Writing clean, maintainable Python code is essential for any developer. Here are some best practices to follow:

## Code Style

Follow PEP 8 guidelines for consistent code formatting. Use meaningful variable names and write clear, concise functions.

## Documentation

Document your code with docstrings and comments. Good documentation makes your code more maintainable and helps other developers understand your intent.

## Error Handling

Always handle exceptions appropriately. Use try-except blocks to catch and handle errors gracefully.

## Testing

Write tests for your code. Testing helps catch bugs early and ensures your code works as expected.

## Performance

Consider performance implications when writing code. Use appropriate data structures and algorithms for your use case.""",
                "excerpt": "Essential Python best practices to write clean, maintainable, and efficient code.",
            },
            {
                "title": "Building REST APIs with Django REST Framework",
                "content": """Django REST Framework (DRF) is a powerful toolkit for building Web APIs. It provides serializers, views, and authentication mechanisms that make API development straightforward.

## Why Use DRF?

- **Serialization**: Convert complex data types to Python native datatypes
- **Authentication**: Built-in authentication classes
- **Permissions**: Flexible permission system
- **Browsable API**: Automatically generated API documentation

## Setting Up DRF

First, install Django REST Framework:

```bash
pip install djangorestframework
```

Add it to your INSTALLED_APPS:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
]
```

## Creating Your First API

Let's create a simple API for a blog application...""",
                "excerpt": "Learn how to build powerful REST APIs using Django REST Framework.",
            },
            {
                "title": "Database Optimization Techniques in Django",
                "content": """Database performance is crucial for web applications. Django provides several tools and techniques to optimize database queries.

## Query Optimization

### Use select_related() and prefetch_related()

These methods help reduce the number of database queries by fetching related objects in advance.

### Database Indexing

Add indexes to frequently queried fields to improve query performance.

### Query Analysis

Use Django's query logging to identify slow queries and optimize them.

## Caching

Implement caching strategies to reduce database load:

- **Page Caching**: Cache entire pages
- **Fragment Caching**: Cache parts of pages
- **Query Caching**: Cache database query results

## Database Connection Pooling

Use connection pooling to manage database connections efficiently.""",
                "excerpt": "Essential techniques for optimizing database performance in Django applications.",
            },
            {
                "title": "Deploying Django Applications to Production",
                "content": """Deploying a Django application to production requires careful planning and configuration. Here's a comprehensive guide to get you started.

## Environment Setup

### Production Settings

Create separate settings files for different environments. Use environment variables for sensitive configuration.

### Static Files

Configure static file serving for production. Use a CDN for better performance.

### Media Files

Set up proper media file handling and storage.

## Web Server Configuration

### Nginx

Configure Nginx as a reverse proxy and static file server.

### Gunicorn

Use Gunicorn as your WSGI server for production.

## Database

### PostgreSQL

PostgreSQL is recommended for production Django applications.

### Database Migrations

Always run migrations in a controlled manner in production.

## Security

- Use HTTPS
- Set secure cookies
- Configure CORS properly
- Use environment variables for secrets""",
                "excerpt": "A complete guide to deploying Django applications to production environments.",
            },
        ]

        # Create posts from templates
        for i, template in enumerate(post_templates):
            if i < count:
                author = random.choice(users)
                slug = slugify(template["title"])

                # Ensure unique slug
                counter = 1
                original_slug = slug
                while Post.objects.filter(slug=slug).exists():
                    slug = f"{original_slug}-{counter}"
                    counter += 1

                # Random publication date within the last 30 days
                days_ago = random.randint(0, 30)
                published_at = timezone.now() - timedelta(days=days_ago)

                post = Post.objects.create(
                    title=template["title"],
                    slug=slug,
                    content=template["content"],
                    excerpt=template["excerpt"],
                    author=author,
                    is_published=random.choice([True, True, True, False]),  # 75% published
                    published_at=published_at if random.choice([True, True, True, False]) else None,
                )
                posts.append(post)

        # Create additional random posts if needed
        remaining_count = count - len(posts)
        for i in range(remaining_count):
            author = random.choice(users)
            title = f"Sample Post {i + 1}"
            slug = slugify(title)

            # Ensure unique slug
            counter = 1
            original_slug = slug
            while Post.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            content = f"""This is sample post content {i + 1}. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Key Points

- This is a sample post
- It contains placeholder content
- It's created for testing purposes

## Conclusion

This concludes our sample post {i + 1}."""

            # Random publication date within the last 30 days
            days_ago = random.randint(0, 30)
            published_at = timezone.now() - timedelta(days=days_ago)

            post = Post.objects.create(
                title=title,
                slug=slug,
                content=content,
                excerpt=f"This is a sample excerpt for post {i + 1}.",
                author=author,
                is_published=random.choice([True, True, True, False]),  # 75% published
                published_at=published_at if random.choice([True, True, True, False]) else None,
            )
            posts.append(post)

        return posts
