#!/bin/bash
holb_user="holberton_user";
replica_user="replica_user"
replica_pass="1234"
root_pass="1234";

mysql -u root -p"$root_pass" <<EOF
CREATE USER IF NOT EXISTS '$replica_user'@'%' IDENTIFIED BY '$replica_pass';
GRANT REPLICATION SLAVE  ON *.* TO '$replica_user'@'%';

GRANT SELECT ON mysql.user TO '$holb_user'@'localhost';
FLUSH PRIVILEGES;
EOF
