README for Library project
# Permissions and Groups

This project implements custom permissions and groups to manage access control:

- **Permissions**: 
  - `can_view`: Allows viewing documents.
  - `can_create`: Allows creating new documents.
  - `can_edit`: Allows editing existing documents.
  - `can_delete`: Allows deleting documents.

- **Groups**:
  - **Viewers**: Can only view documents.
  - **Editors**: Can view, create, and edit documents.
  - **Admins**: Have all permissions including deleting documents.

Permissions are enforced using Django’s `@permission_required` decorator in views.

This Django project implements several security best practices:

1. Secure Settings:
   - DEBUG is set to False in production.
   - Browser security headers (XSS Filter, X-Frame-Options, Content-Type-Nosniff) are enabled.
   - CSRF and Session cookies are set to secure (HTTPS only).

2. CSRF Protection:
   - All forms include {% csrf_token %} to protect against CSRF attacks.

3. Secure Data Access:
   - Views use Django's ORM for safe querying to prevent SQL injection.
   - User inputs are validated and sanitized using Django forms.

4. Content Security Policy (CSP):
   - CSP headers are set to restrict content sources and mitigate XSS risks.

5. Input Validation:
   - Forms include server-side validation to ensure data integrity and security.

To test these security measures:
1. Ensure DEBUG is False in production settings.
2. Verify that all forms include CSRF tokens.
3. Test search functionality with various inputs to ensure safe handling.
4. Check browser headers to confirm CSP and other security headers are present.
5. Attempt to submit forms with malicious content to verify input validation.

Remember to regularly update Django and all dependencies to patch any known vulnerabilitie