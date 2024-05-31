# 1. Distributed web infrastructure 

### For every additional element, why you are adding it
- loader handler : for handle excessive requests
- a server : distribute the request with the one server
### What distribution algorithm your load balancer is configured with and how it works
I choice Round Robin: first request go to the first server second to the second server and so on.
### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
- 1 active-active  : all servers handle the requests
- 2 active-passive : one or more servers handle the requests and others are passive until the active servers fail
### How a database Primary-Replica (Master-Slave) cluster works
- master: handle the (update, create, delete, read) all operations
- slave : handle only read opertion to make the database faster by get it only necessary requests
### What is the difference between the Primary node and the Replica node in regard to the application

### You must be able to explain what the issues are with this infrastructure:
- Traffic encryption
- firewall for safety for mallicious requests
- large scale need more servers 
- handle the server by common command line.
### Where are SPOF
- the one that have only one server : load balancer
