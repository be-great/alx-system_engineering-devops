##  12. Tell the story of passwd 

    john:x:1001:1001:John Doe:/home/john:/bin/bash
    
1- Username: john

2-Password Placeholder: x (password stored in /etc/shadow)

3- UID: 1001 (user id)

4- GID: 1001 (group id)

5- User Info (comments): John Doe 

6- Home Directory: /home/john

7-Login Shell: /bin/bash

### search for a User:-

    grep john /etc/passwd

### search multiple users:-

    egrep -w '^(john|ahed|fox)' /etc/passwd

### IFS separator:-

##### it's away of splits words like (string.split(",") in python) , Example:-

    string = "hello workd, how are me?!"
    IFS=',' read -ra words <<< "$string"
    for word in "${words[@]}";do
        echo "$word"
    done

##### Example of reading: /etc/passwd and save each field on variables f1, f2, f3,...,f7

    while IFS=: read -r f1 f2 f3 f4 f5 f6 f7
    do
        echo "User:$f1:dir:$f7"
    done < /etc/passwd



##  13. Let's parse Apache logs 

    