# REAME
## TASK 0
- https://computingforgeeks.com/how-to-install-mysql-on-ubuntu-focal/
- https://itsfoss.com/solve-gpg-error-signatures-verified-ubuntu/

## TASK1
- CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'PASSWORD';
- GRANT REPLICATION CLIENT ON . TO holberton_user@localhost;
- SELECT User FROM mysql.user;
- SHOW GRANTS FOR holberton_user@localhost;

# TASK3
- CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'PASSWORD';
- GRANT REPLICATION CLIENT ON . TO 'replica_user'@'%';
- GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
- GRANT REPLICATION SLAVE ON . TO 'replica_user'@'%';
