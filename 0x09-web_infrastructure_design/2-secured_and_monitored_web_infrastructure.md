# Explanation of Infrastructure

## Components and Roles

### Firewalls (3):

Purpose: Protect the network by filtering incoming and outgoing traffic based on security rules, preventing unauthorized access and attacks.

### Load Balancer (HAProxy):

Role: Distributes incoming traffic across all servers to ensure high availability and reliability.

### Distribution Algorithm:

Round Robin: Evenly distributes incoming requests across all available servers in a sequential manner.

### Servers:

Each runs Nginx as the web server, the application server, and Runs MySQL as the database server and has monitoring clients installed to collect performance data.

### SSL Certificate:

Role: Encrypts traffic between users and the website to ensure data privacy and security.

Placement: Installed on the load balancer to serve HTTPS traffic.

### Monitoring Clients:

Role: Collect and send performance and health metrics to a monitoring service like Sumologic.

Placement: Installed on all servers (Server 1, Server 2, and Server 3).

## Specific Explanations

### HTTPS Traffic:
Purpose: Encrypts data in transit to protect sensitive information from eavesdropping and tampering, ensuring secure communication between users and the website.

### Monitoring:

Purpose: Monitoring helps maintain the health, performance, and availability of the infrastructure by collecting and analyzing various metrics.

  Data Collection: Monitoring clients collect data on CPU usage, memory usage, disk I/O, network traffic, and application performance. This data is sent to a centralized monitoring service like Sumologic for analysis and alerting.

### Monitoring QPS (Queries Per Second):

 - Action: Set up custom metrics in the monitoring clients to track the number of queries handled by the web servers per second. This data can be visualized and used to set up alerts in the monitoring service.
 - 
## Issues with This Infrastructure

### Terminating SSL at the Load Balancer:

 - Issue: Traffic between the load balancer and the backend servers is not encrypted, potentially exposing sensitive data if intercepted.
   
 - Solution: Use SSL/TLS to encrypt traffic between the load balancer and backend servers.
   
### Single MySQL Server for Writes:

 - Issue: Creates a single point of failure. If the MySQL server fails, write operations will fail, leading to potential data loss or downtime
   
 - Solution: Implement a Primary-Replica (Master-Slave) setup to distribute write and read operations and provide redundancy.
   
### Homogeneous Servers (Database, Web Server, Application Server):

 - Issue: Combining all components on the same servers can lead to resource contention, where high load on one component affects the performance of others. This also complicates scaling and maintenance.
   
 - Solution: Separate the components onto dedicated servers for the web server, application server, and database server to improve performance and scalability.
