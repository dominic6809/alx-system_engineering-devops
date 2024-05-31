# Explanation of Infrastructure

## Components

### Server:

Definition: A server is a computer designed to process requests and deliver data to other computers over a local network or the internet. In this case, it's a single machine hosting all necessary components for the website.

### Domain Name:

Role: The domain name foobar.com is a human-readable address that users type into their web browsers to access the website. It translates into the server's IP address using DNS.

### DNS Record:

Type: The www in www.foobar.com is a CNAME (Canonical Name) or an A (Address) record that maps the domain name to the server's IP address (8.8.8.8).

### Web Server (Nginx):

Role: Nginx is responsible for handling HTTP requests from users, serving static content (like HTML, CSS, JavaScript), and acting as a reverse proxy to forward requests to the application server.

### Application Server:

Role: The application server runs the business logic of the website, processes dynamic requests, and generates responses. It executes the code base, interacting with the database when necessary.

### Application Files (Code Base):

Role: These are the files containing the website's code, including HTML, CSS, JavaScript, and server-side scripts. The application server executes this code to serve dynamic content to users.

### Database (MySQL):

Role: MySQL stores and manages data required by the website, such as user information, posts, comments, etc. It processes SQL queries from the application server to retrieve or update data.

### Communication:

Protocol: The server communicates with the user's computer over the internet using the HTTP/HTTPS protocols. When a user requests a page, the web server (Nginx) responds to the request by serving the appropriate content.

## Specifics and Issues

### Type of DNS Record
  www in www.foobar.com:
Type: Commonly a CNAME or A record.

Purpose: Maps the subdomain www to the server's IP address (8.8.8.8).

### Role of the Web Server

Definition: Manages HTTP requests, serves static content, and forwards dynamic requests to the application server.

### Role of the Application Server

Definition: Processes business logic, handles dynamic content, and interacts with the database to generate responses.

### Role of the Database

Definition: Stores and manages data, processes queries from the application server to retrieve or update information.

### Communication with User's Computer

Protocol: Uses HTTP/HTTPS to communicate over the internet.

# Issues with This Infrastructure
## Single Point of Failure (SPOF):

Issue: The entire website relies on one server. If the server fails, the website becomes unavailable.

## Downtime During Maintenance:

Issue: Any maintenance activity, such as deploying new code, requires restarting the server, causing temporary downtime.

## Scalability:

Issue: A single server cannot handle a high volume of incoming traffic. As traffic increases, the server may become overwhelmed, leading to performance degradation or outages.
