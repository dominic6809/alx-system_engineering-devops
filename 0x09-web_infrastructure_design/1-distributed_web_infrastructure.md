# Explanation of Infrastructure

## Components and Roles

### Load Balancer (HAProxy):

Role: Distributes incoming HTTP/HTTPS requests across multiple servers to ensure high availability and reliability.

### Distribution Algorithm:

Round Robin: This algorithm cycles through the available servers in order, distributing each incoming request to the next server in the list. This helps to evenly distribute the load across all servers.

### Servers:

 - #### Server 1 & Server 2:

  - Role: Each server runs Nginx as the web server and hosts the application server and application files (code base). They handle incoming web traffic and process application logic.

 - #### Server 3:

Role: Runs MySQL as the database server. It stores and manages the application's data.

### Application Files (Code Base):

Role: These files contain the website's code, which includes HTML, CSS, JavaScript, and server-side scripts. They are deployed on Server 1 and Server 2.

### Database (MySQL):

Role: Manages and stores the data needed by the application.

## Specific Explanations

### Load Balancer Configuration:

 - Distribution Algorithm: The load balancer is configured with a Round Robin algorithm. This ensures that incoming requests are distributed evenly across Server 1 and Server 2, preventing any single server from becoming overloaded.

### Active-Active vs. Active-Passive Setup:

 - Active-Active: Both Server 1 and Server 2 are actively handling requests at the same time, providing load distribution and redundancy.

 - Active-Passive: One server handles all the requests while the other remains idle until the active server fails. This design uses Active-Active to ensure both servers are utilized and provide redundancy.

### Database Primary-Replica (Master-Slave) Cluster:

 - How it Works: The Primary (Master) node handles all write operations and replicates data to one or more Replica (Slave) nodes, which handle read operations. This separation of read and write operations can improve performance and provide data redundancy.

 - Primary Node: Handles all the write operations and ensures data consistency.
  
 - Replica Node: Handles read operations and replicates data from the Primary node, reducing the load on the Primary node and providing redundancy.
   
# Issues with This Infrastructure

## Single Points of Failure (SPOF):

### Load Balancer: If the load balancer fails, no traffic can reach the web servers.

### Database: If the single MySQL server fails, the application cannot access its data.

## Security Issues:

 - No Firewall: Without a firewall, the infrastructure is vulnerable to unauthorized access and attacks.
   
 - No HTTPS: Without HTTPS, data between the users and the server is not encrypted, making it susceptible to interception and tampering.
   
 - No Monitoring:

Issue: Without monitoring, there is no way to track the health, performance, and availability of the servers, making it difficult to detect and respond to issues promptly.
