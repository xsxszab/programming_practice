#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE* fp;
	if((fp=fopen("test2.txt","w+"))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	fprintf(fp,"haha\n");
	fprintf(fp,"%d %d %d\n",1,2,3);
	fprintf(fp,"hahahaha\n");
	fclose(fp);
	char c;
	if((fp=fopen("test2.txt","r"))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	while(1)
	{
		c=fgetc(fp);
		if(feof(fp))
		{
			printf("------------------\ndone\n");
			break;
		}
		printf("%c",c);
	}
	fclose(fp);
	return 0;
}
