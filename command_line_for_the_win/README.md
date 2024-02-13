#  Command line for the win
<a href="https://cmdchallenge.com">CMD CHALLENGE</a> is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated.


# Steps to upload the screenshots using SFTP into the sandbox enviroment :-

1- Connect to the Remote Server:

	$ sftp username@hostname

Enter Password: You will be prompted to enter your password.

2- Navigate to the Remote Directory:

	$ cd /path/to/remote/directory

Use the cd command to navigate to the directory where you want to upload the files.

3- Upload Files:

	$ put *

4- Close the SFTP session:

	$ exit


