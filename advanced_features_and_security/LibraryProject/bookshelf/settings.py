UTH_USER_MODEL = 'users.CustomUser'["bookshelf.CustomUser"]

DEBUG = False

# Prevent XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent the site from being embedded in iframes
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enforce secure cookies over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Enable HTTPS-only for CSRF tokens
CSRF_COOKIE_HTTPONLY = True

MIDDLEWARE = [
    # ... other middleware ...
    'csp.middleware.CSPMiddleware',
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_SCRIPT_SRC = ("'self'",)

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ... (other middleware)
]

# Set allowed hosts
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

