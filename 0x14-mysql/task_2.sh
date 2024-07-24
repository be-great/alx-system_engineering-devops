#!/bin/bash
holb_user="";
holb_pass="";
root_pass="";

mysql -u root -p"$root_pass" <<EOF
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
INSERT INTO nexus6 (name) VALUES ('Leon');
GRANT SELECT ON tyrell_corp.nexus6 TO '$holb_user'@'localhost';
FLUSH PRIVILEGES;
EOF
