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
