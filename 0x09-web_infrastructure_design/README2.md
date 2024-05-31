# 2. Secured and monitored web infrastructure 
    
### For every additional element, why you are adding it
- firewall : protect the user from malicious requests. 
- ssl: encrypte traffic
### What are firewalls for
protoct from networks from unauthorized access, cyber threats, and data breaches,
### Why is the traffic served over HTTPS

because it encrypte the request being sended and protect the data from like man-in-the-middle.
- CPU use
- log forwarding
### How the monitoring tool is collecting data
- API agents 
- load forwarder
### Explain what to do if you want to monitor your web server QPS
- configure Sumologic to collect the log and visualize the data and set alerts on specific failer
### Why terminating SSL at the load balancer level is an issue
- will break the end-end encryption
### Why having only one MySQL server capable of accepting writes is an issue
- Single Point of Failure
- load overdose.
### Why having servers with all the same components (database, web server and application server) might be a problem
- Uniform Vulnerability