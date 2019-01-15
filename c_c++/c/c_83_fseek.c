#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE* fp;
	if((fp=fopen("test1.txt","r"))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	fseek(fp,6,SEEK_SET);
	char c;
	c=fgetc(fp);
	printf("%c\n",c);
	rewind(fp);
	fseek(fp,-2,SEEK_END);
	c=fgetc(fp);
	printf("%c\n",c);
	fclose(fp);
	return 0;
}
