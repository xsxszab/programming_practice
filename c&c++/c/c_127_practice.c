#include<stdio.h>
#include<string.h>

int main()
{
	char str[]="The fucking C exam";
	char *p1,*p2;
	p1=strchr(str,'e');
	p2=strrchr(str,'e');
	printf("%s\n%s\n",p1,p2);
	return 0;
}
