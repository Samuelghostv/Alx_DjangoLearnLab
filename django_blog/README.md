## Documentation overview

The authentication system consists of four main functionalities, registration, login, logout and profile
management.

User can create account, login in, logout, and update their profiles with additional field like email and bio.

## Setup Instruction

Ensure Django is installed.
create the CustomUserCreationform and UserProfile model.
Define views for registration, login, logout and profile management.
Create corresponding HTML templates
Configure URLS in urls.py

## Testing the Authentication Features

Registration: Ensure users can successfully register.
Login/logout: Test login/logout redirect and sessions management
Profile Management: Testing updating the profile information
Security: Test CSRF protection and password security

## Blog post management feature doc

This is a sample blog application where users can create, read, update, and delete posts

- **Post List**: View all blog posts with a title and snippet of content.
- **Post Detail**: View the full content of blog posts.
- **Create Post**: Authenticated user can create new posts.
- **Edit Post**: Only authors can edits their post.
- **Delete Post**: Only authors can delete their posts