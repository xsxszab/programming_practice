#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE* fp;
	if((fp=fopen("test3.txt","w"))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	fputs("abcd",fp);
	fclose(fp);
	return 0;
}
