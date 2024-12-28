You will need to create documentation that describes the authentication system:

## Explanation of Authentication Flow:

The registration view is accessible via /register, where users can create new accounts.
Login is done through /login, where users enter their username and password.
Logout is handled by Django's built-in logout view, accessible at /logout.
Profile management is available at /profile, where users can update their email and other details.
Testing Authentication Features:

Registration: Test by creating a new user via /register.
Login/Logout: Test by logging in at /login and logging out using the logout button or by visiting /logout.
Profile Update: After logging in, visit /profile to test updating user details.
