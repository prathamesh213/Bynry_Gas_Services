# Bynry_Gas_Services
gas_utility_service/
├── gas_utility/                # Main Django project
│   ├── settings.py             # Django project settings
│   ├── urls.py                 # Project-level URL routing
│   ├── wsgi.py                 # WSGI configuration for deployment
│   └── asgi.py                 # ASGI configuration for asynchronous support
├── accounts/                   # Manages user accounts
│   ├── templates/              # Templates specific to accounts
│   ├── urls.py                 # URL routing for accounts app
│   ├── views.py                # Handles account-related views
│   └── models.py               # Database models for user accounts
├── service_requests/           # Handles service requests functionality
│   ├── templates/              # Templates for service requests
│   ├── urls.py                 # URL routing for service requests app
│   ├── views.py                # Handles views for service requests
│   ├── forms.py                # Django forms for service request submissions
│   └── models.py               # Database models for service requests
├── support/                    # Customer support representative tools
│   ├── templates/              # Templates for support
│   ├── urls.py                 # URL routing for support app
│   ├── views.py                # Handles views for support representatives
│   └── models.py               # Models for tracking internal operations
├── templates/                  # Global templates shared across the app
│   ├── base.html               # Base template for consistent layout
│   ├── home.html               # Home page template
│   └── error.html              # Error handling template
├── manage.py                   # Django’s command-line utility
├── db.sqlite3                  # SQLite database (default for development)
