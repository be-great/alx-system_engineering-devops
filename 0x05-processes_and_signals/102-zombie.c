#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
* infinite_while - makes infinite_while
* Return: 0 loop finish
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - create 5 process
* Return: 0 Always(Success)
*
*/
int main(void)
{

	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i++;
		}
		else
		{
			exit(0);
		}
	}


	infinite_while();
	return (EXIT_SUCCESS);

}
