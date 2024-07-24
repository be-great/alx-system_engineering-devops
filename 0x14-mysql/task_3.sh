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
CHANGE MASTER TO MASTER_HOST='34.232.76.39', MASTER_USER='replica_user', MASTER_PASSWORD='1234', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=433;
