# 0x14. MySQL 

## General

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to  - make sure that your database backup strategy actually works

## different between Replication slave , Replication client
- REPLICATION SLAVE: Needed to set up and manage slave servers, allowing access to binary logs and replication commands.
- REPLICATION CLIENT: Used for monitoring replication status and logs without the ability to alter replication settings.
```sql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
/*++++++++++++++++++++++++++++++++++++++++++++++++*/
CREATE USER 'monitor_user'@'localhost' IDENTIFIED BY 'monitor_password';
GRANT REPLICATION CLIENT ON *.* TO 'monitor_user'@'localhost';

```
- the primary database is in web-01 and the replica must be in the web-02 so: (web-01 == client , web-02 == slave)