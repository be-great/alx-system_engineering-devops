#  0x1A. Application server 
### Application server vs web server
- Web server is static files like (html, css, javaScript).
- Application server is a dynamic content (use databases , api) like flask as application server or Apache Tomcat

## Example setup Medifycare
```bash
sudo pip install -r requirements.txt
sudo nano /etc/systemd/system/medifycare.service
```
```txt
[Unit]
Description=Gunicorn instance to serve my_flask_app
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/ubuntu/MedifyCare
Environment="PATH=/home/ubuntu/MedifyCare/venv/bin"
Environment="WEBAPP_ENV=prod"
Environment="WEBAPP_ENV=prod"
Environment="STRIPE_PUBLISHABLE_KEY=****"
Environment="STRIPE_SECRET_KEY=****"
ExecStart=/usr/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl restart medifycare
sudo systemctl status medifycare
```
```bash
sudo nano /etc/nginx/sites-enabled/default
```
```txt
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By 518598-web-01;
    root   /var/www/html;
    index  index.nginx-debian.html index.nginx-debian.htm;

    location /redirect_me {
        return 301 http://github.com/;
    }

    location / {
        proxy_pass http://0.0.0.0:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
```
```bash
sudo systemctl restart nginx
```
