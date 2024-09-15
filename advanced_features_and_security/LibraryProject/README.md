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
