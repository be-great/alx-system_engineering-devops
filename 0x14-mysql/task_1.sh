#!/bin/bash
pass="****"
user="root"
holb_user="holberton_user"
holb_pass="****"
mysql -u root -p$pass -e "
CREATE USER IF NOT EXISTS '$holb_user'@'localhost' IDENTIFIED BY '$holb_pass';
GRANT REPLICATION CLIENT ON *.* TO '$holb_user'@'localhost';
FLUSH PRIVILEGES;
"


