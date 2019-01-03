#include<stdio.h>

int main()
{
	char str1[5]={'a','b','c','d'};
	puts(str1);
	printf("%d",str1[4]);
	char *str2="asldfjgosreb";
	char str3[]="sdgerhtrh";
	//wrong: str2[1]='a';
	//wrong: str3[1]='a';
	puts(str2);
	puts(str3);
	return 0;
}
