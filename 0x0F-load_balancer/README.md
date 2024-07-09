# 0x0F. Load balancer:-
<img src="load_balancer.png"></img>

- Software load balancer.
### Algorithms that used by the load balancer
1. Weighted Scheduling Algorithm: each task has a weight represent it's priority and the task with the highest weight execute first
2. Round Robin Scheduling: each task has a fixed time slice and the first task in the queue execute first as (FIFO).
3. Least Connection First Scheduling: If there is a task coming the load balancer see which server has the fewest active connection and send the task to it . within each server the order of task execution depend on the internal scheduling algorithm. 
- Hardware load balancer.
### load balancer in OSI Layers
1. layer 2 (Data Link Layer)  : forward packets based on MAC addresses
2. Layer 3 (Network Layer)    : forward packets based on IP addresses
3. Layer 4 (Transport Layer)  : forward packets based on IP addresses and port number
4. Layer 7 (Application Layer): Examine content HTTP headers, sessions, cookies, etc.
```bash
frontend http
    bind *:80   => handle traffic on port 80
    mode http   => handle traffic on http protocol mode

    acl url_blog path_beg /blog    => matches requests that has the url begins with /blog
    use_backend blog-backend if url_blog => pass the traffic to blog-backend
    default_backend web-backend => all other traffic that doesn't match send it to web-backend
```
## HAProxy and Load Balancing:-
HAProxy: High Availabity Proxy (gateway between a client and another server for security reasons). is a software for load balancing and proxy solution.
### concepts:-
1. Access Control List (ACL)

```bash
acl url_blog path_beg /blog
# match url that start with /blog
http://exmaple.com/blog/post1
http://exmaple.com/blog/category/tech

```
- url_blog: the rule name or condition name
- path_beg: conditon based on the beginning of url path.
- /blog: the string that checks against path_beg

2. Backend : load balancer algorithm to use, list of server and ports to use
```bash
backend web-backend
    balance roundrobin                   => the algorithm
    server web1 web1.domain.com:80 check => check health server in it
    server web2 web2.domain.com:80 check => check health server in it
backend blog-backend
    balance roundrobin
    mode http                              => specify layer 7 will be used
    server blog1 blog1.domain.com:80 check => check health server in it
    server blog2 blog2.domain.com:80 check => check health server in it

```
3. Frontend: defined how the request should pass to the backends
   - a set of IP addresses and port (ip_address:80)
   - ACLs 
   - use_backend rules: define which backends ACLs conditions are matched

##### Note: *All scripts designed to configure a brand new Ubuntu server to match each task requirements.*
## Task 0.
The goal here is to be able to track which web server is answering our HTTP requests

## Task 1.


## Task 2.


