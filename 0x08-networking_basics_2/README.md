#  0x08. Networking basics #1 

## ifconfig 
- dispaly information about network interfaces
- Examples:-

    ifconfig 
    ifconfig eth0

## telent
- establish a connection to a remote server on specfic port
- Examples:-

    telnet google.com 80
    telnet 192.168.1.100 22

## nc (netcat)
- reading and writing to network connection (TCP, UDP)
- port scanning, send files, backdoors
- Example,  listen on specific port :-

    nc -l 1234

## cut 
- The cut command is used to extract sections from each line of input files and write them to the standard output.
- Examples:-

     cut -d' ' -f2,3 filename.txt
