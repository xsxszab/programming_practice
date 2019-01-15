#include<stdio.h>

int main()
{
	char str1[]="abcd";
	char str2[]={'a','b','c','d'};
	puts(str1);
	puts(str2);
	printf("%ld\n",sizeof(str1));
	printf("%ld\n",sizeof(str2));
	return 0;
}
