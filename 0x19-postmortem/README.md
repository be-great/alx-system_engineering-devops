# Postmortem : Reports
## Summary
On our WordPress website, an internal Server Error was down the server.

<img src="img/error.png">

- Duration of the outage: Aug 12, 2024, 6:00 AM - Aug 19, 2024, 6:00 AM
- The impact: down the hole services, The user was experiencing 500 internal error codes.

## Timeline
- 15/08 - the issue was detected on 15/08, the issue detected by curling the prime server IP address, we assumed that the apaches server that running the WordPress website had a problem, The incident was resolved by  watching how the program interacted with the system using `strace` command. 
## Root cause
- to resolve the problem first we use the tmux command to have split windows for better capturing the problem by eyes. 
<img src="img/tmux.png">
- then we search the process that runs the Apache services.
```bash
ps -aux | grep apache
```
- then we copy the PID and see how the system reacts to the user getting the services
```bash
# in window one 
sudo strace -p <pid>
# in the other window
curl -sI 127.0.0.1
```
<img src="img/curl_strace.png">
<img src="img/strace.png">

### As we see we get a file not found `class-wp-locale.phpp` and that's a wrong php extension 

- then we need to search where this file initialized
<img src="img/search_file.png">

- Searching each file for the file name `class-wp-locale.phpp`
<img src="img/inside_the_file.png">

## Corrective and preventative measures must contain
- We most create a todo list for similar failure , for this problem the problem can be listed in todo format :-
    -   checking each file extensions
    -   correct it if it's wrong
