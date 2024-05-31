#  0x09. Web infrastructure design 


## DNS
- -------computer-----|-----DNS server------|----google----|
- | www.google.com  =>  www.google.com => google    | 
- | www.google.com  <=  192.123.23.23 <= 192.123.23.23"|
- ---------------------------------------------------------

- Note:  DNS servers do not typically store IP addresses in their databases. but get it from authoritative DNS servers that store that connection

<img src="imgs/DNS.png">

## Monitoring

- Tracking the performance and availability of (Systems, networks, applications)

## Web Server
- software serves web pages to browser http/https

## Load Balancer
- split the netwrok traffic into mulitple server to reduce the overwhelmed of just one server
<img src="imgs/LoadBalancer.png">
## Server
- computer or software that provides services.
## LAMP
- Stand For  : Linux, Apache, MySQL, Perl/PHP/Python
- Design for :  open source software to build web applications
<img src="imgs/LAMP.png">
