#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE* fp;
	char s1[10],s2[10],s3[10],s4[10];
	if((fp=fopen("test1.txt","r"))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	fscanf(fp,"%s%s%s%s",s1,s2,s3,s4);
	printf("%s\n%s\n%s\n%s\n",s1,s2,s3,s4);
	return 0;
}
