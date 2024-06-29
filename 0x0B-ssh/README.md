#  0x0B. SSH 

## General

- What is a server
a server is a computer system or a software provide a resoures or service for other computers
- Where servers usually live
data center
- What is SSH
is cryptographic network protocal used for secure the communication between client and the server.
- How to create an SSH RSA key pair
RSA is consist of two key : private and public key
- How to connect to a remote host using an SSH RSA key pair
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# Copy the public key to the remote url
ssh-copy-id user@remote_host
# Connect
ssh user@remote_host
```
- The advantage of using #!/usr/bin/env bash instead of /bin/bash
```bash
- #!/usr/bin/env bash This approach is especially useful in environments like virtual environments 
```
