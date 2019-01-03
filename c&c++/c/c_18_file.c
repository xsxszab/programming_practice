#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE *fp;
	if((fp=fopen("test2.txt","w"))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	const char line1[]="ahuiaw\n";
	const char line2[]="gwegergerrehrt\n";
	const char line3[]="2134rt3gtrhbt\n";
	fputs(line1,fp);
	fputs(line2,fp);
	fputs(line3,fp);
	fclose(fp);
	return 0;
}
