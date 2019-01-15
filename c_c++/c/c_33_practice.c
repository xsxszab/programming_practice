#include<stdio.h>
#include<string.h>

int main()
{
	char str[100];
	gets(str);
	int i,j;
	char temp;
	i=0;
	j=strlen(str)-1;
	while(i<j)
	{
		temp=str[i];
		str[i++]=str[j];
		str[j--]=temp;
	}
	puts(str);
	return 0;
}
