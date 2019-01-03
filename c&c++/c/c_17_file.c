#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE *fp;
	if((fp=fopen("./test1.txt","r"))==NULL)
	{
		printf("cannot open this file\n");
		exit(1);
	}
	char ch=fgetc(fp);
	while(ch!=EOF)
	{
		putchar(ch);
		ch=fgetc(fp);
	}
	fclose(fp);
	return 0;
}
