# Project 0x09: Web Infrastructure Design

## Overview

This project involves designing a secure, scalable, and monitored web infrastructure for hosting the website www.foobar.com. The infrastructure consists of multiple servers, firewalls, SSL encryption, and monitoring components.

## Infrastructure Components

### Servers
- **Server 1**: Web Server, Application Server, Monitoring Client
- **Server 2**: Web Server, Application Server, Monitoring Client
- **Server 3**: Web Server, Application Server, Monitoring Client

### Firewalls
- **Firewall 1**: Between the internet and the load balancer.
- **Firewall 2**: Between the load balancer and Server 1.
- **Firewall 3**: Between the load balancer and Server 2.
- **Firewall 4**: Between the load balancer and Server 3.

### Load Balancer
- **Purpose**: Distributes incoming traffic across the servers to ensure high availability and reliability.

### SSL Certificate
- **Purpose**: Encrypts traffic to and from the website to ensure data privacy and security.
- **Location**: Installed on the load balancer.

### Database
- **MySQL Server**: Single database server for handling data storage.

### Monitoring
- **Sumologic**: Used for monitoring and collecting metrics from each server.

## Detailed Explanations

### Firewalls
- **Purpose**: Protect the network by filtering traffic based on security rules.
- **Explanation**: Firewalls help to prevent unauthorized access, DDoS attacks, and other security threats by filtering traffic based on predefined rules.

### HTTPS Traffic
- **Purpose**: Encrypts data between the client and the server.
- **Explanation**: Serving traffic over HTTPS ensures that sensitive information such as login credentials and personal data are protected from eavesdropping and tampering.

### Monitoring
- **Purpose**: Maintains system health, performance, and availability.
- **Explanation**: Monitoring clients collect data on CPU usage, memory usage, disk I/O, network traffic, and application performance. This data is sent to Sumologic for analysis and alerting.

### Monitoring QPS (Queries Per Second)
- **Action**: Set up custom metrics in the monitoring clients to track the number of queries handled by the web servers per second.

## Issues and Considerations

### Terminating SSL at the Load Balancer
- **Issue**: Traffic between the load balancer and the backend servers is not encrypted.
- **Solution**: Use SSL/TLS to encrypt traffic between the load balancer and backend servers as well.

### Single MySQL Server for Writes
- **Issue**: Single point of failure for write operations.
- **Solution**: Implement replication and failover strategies to ensure high availability and reliability.

### Homogeneous Servers
- **Issue**: Resource contention and complexity in scaling and maintenance.
- **Solution**: Separate concerns by using dedicated servers for different components (e.g., web servers, application servers, database servers).

## Resources for Creating Infrastructure Diagrams

Here are some tools you can use to create and customize infrastructure diagrams:

- [Lucidchart](https://www.lucidchart.com/)
- [Draw.io (diagrams.net)](https://www.draw.io/)
- [Microsoft Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software)
- [Gliffy](https://www.gliffy.com/)
- [Creately](https://www.creately.com/)
- [Cacoo](https://cacoo.com/)

## Conclusion

This project outlines a secure, scalable, and monitored web infrastructure for hosting www.foobar.com. Proper implementation of firewalls, SSL encryption, and monitoring ensures the reliability, security, and performance of the website. Addressing potential issues such as SSL termination, single MySQL server, and resource contention is crucial for optimal operation.
