# Test: API Request Sequence

Create a Mermaid sequence diagram for this interaction:

A user logs into a web application:
1. User enters credentials in the browser
2. Browser sends login request to API server
3. API server queries the database to verify credentials
4. Database returns user record (or not found)
5. API server creates session token
6. API server returns token to browser
7. Browser stores token and redirects to dashboard

Requirements:
- Three participants: User/Browser, API Server, Database
- Show request and response arrows
- Use async notation for database query
