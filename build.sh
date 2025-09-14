#!/bin/bash

# Upgrade Resources
pip install --upgrade pip
pip install uv

# Install dependencies
echo "Installing dependencies..."
source "${VENV_ROOT}/bin/activate"
uv sync

# Apply database migrations
echo "Applying database migrations..."
uv run manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
uv run manage.py collectstatic --noinput

# Create superuser if admin user doesn't exist
echo "Checking for admin user..."
ADMIN_EXISTS=$(uv run manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
print('true' if User.objects.filter(username='admin').exists() else 'false')
")

if [ "$ADMIN_EXISTS" = "false" ]; then
    echo "Creating admin superuser..."
    uv run manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
print('Admin user created successfully')
"
else
    echo "Admin user already exists, skipping superuser creation"
fi
