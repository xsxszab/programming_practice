#include<stdio.h>
#include<string.h>

int main()
{
	char str[20]="abcdefg";
	printf("%ld\n",strlen(str));
	printf("str: %s\nstr+1: %s\nstr+2: %s\n------------\n",str,str+1,str+2);
	strcpy(str+1,str+2);
	printf("%s\n",str);
	return 0;
}
