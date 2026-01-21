import pytest
import django
from django.conf import settings

# Configure Django settings for tests
if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "rest_framework",
            "order",
            "product",
        ],
        SECRET_KEY="test-secret-key",
        USE_TZ=True,
    )
    django.setup()
