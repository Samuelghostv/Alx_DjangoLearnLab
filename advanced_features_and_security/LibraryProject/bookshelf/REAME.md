### Custom Permissions and Groups in the "bookshelf app
1. **Custom Permissions**:
   - Defined in the `News` model: 
   'can_view' : Allows users to views a News
   'can_create' : Allows users to create a News
   'can_edit' : Allows users to edit a News
   'can_delete' : Allows users to views a News

2. **Groups and Permissions**:
   - **Editor**: Assign 'can_create' and 'can_edit' permissions.
   - **Viewers**: Assign `can_view`, permissions.
   - **Admins**: Assign to all permissions that anyone can do

3. **Views**:
   - The following views are permission-protected
   - 'create_news' : Required 'can_create' permission.
   - 'edit_news'   : Required 'can_edit' permissions
   - 'view_news'   : Required  'can_view' permissions
   - 'delete_news'  : Required  'can_delete' permissions

   **Testing**
   - create test users in Django admin and assign them to groups (Views, Editors, Admins).
   - log in as different user in a specific groups and test the ability to perform actions like creating, editing, viewing, and deleting news. Ensure the permissions are well applied to them
