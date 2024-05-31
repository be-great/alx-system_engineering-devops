#  0. Simple web stack :-

### What is a server
A computer or software that provides services.
### What is the role of the domain name
is a human readable identifer for online resources or a website
### What type of DNS record www is in www.foobar.com
CNAME Record (Canonical Name Record): Creates an alias for a domain name, redirecting it to another domain.
### What is the role of the web server
A computer or software that provides web pages for users.

### What is the role of the application server
The role of it managing web applications 
### What is the role of the database
the role of the database is to store data
### What is the server using to communicate with the computer of the user requesting the website
HTTP/HTTPs they are protocol to exhange data on the web.
### SPOF
stand : a Single Point of Failure.If one server like DNS failed should not Fail our services (relabity).
### Downtime when maintenance needed (like deploying new code web server needs to be restarted)
if we need some update we Down the server through the deploying the new code then start it
### Cannot scale if too much incoming traffic
if our business reaches a lot of users the server should be scaled to handle the massive requests one solution would be a load balancer which distrupte the request into multiple servers not one for the same service.