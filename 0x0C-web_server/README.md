#  0x0C. Web server 

## scp:-
SCP uses SSH for authentication and data encryption, ensuring that files are transferred securely
- send a file to another computer or server using ssh with passed private key.
```bash
$ scp -o StrictHostKeyChecking=no -i path_to_privatekey file "ubuntu@$10.100.22.0:~/";
```
## Nginx:-
 - It reverse proxy (server that sits in front of web servers and forwards client), load balancing, caching
 - Example: install nginx and replace the html of nginx to "Hello, World!"
```bash
sudo apt-get -y update
sudo apt-get install -y nginx
sudo service nginx start
echo "Hello World!" > /var/www/html/index.nginx-debian.html
sudo service nginx restart
```
