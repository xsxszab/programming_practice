#include<stdio.h>

int main(int argc,char *argv[])
{
	if(argc==1)
	{
		printf("no input\n");
		return 1;
	}
	if(argc==2)
		printf("the argument is %s\n",argv[1]);
	else
		printf("too many arguments\n");
	return 0;
}
