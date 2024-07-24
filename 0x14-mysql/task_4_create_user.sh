#!/bin/bash
# In web-01
root_pass="1234";
# In web-02
mysql -u root -p"$root_pass" <<EOF
CHANGE MASTER TO MASTER_HOST='<ip_web-01>', MASTER_USER='slave', MASTER_PASSWORD='slavepass', MASTER_LOG_FILE='<"show master status" in web-01 and copy the file name >', MASTER_LOG_POS=<the position after you exe the show master status on web-01>;
START SLAVE;
EOF
sudo service mysql restart
