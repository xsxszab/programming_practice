#include<stdio.h>
#include<string.h>

void judge(char str[])
{
	int i,j;
	int flag=1;
	i=0;
	j=strlen(str)-1;
	while(i<=j)
		if(str[i++]!=str[j--])
		{
			flag=0;
			break;int i,j;
	int flag=1;
	i=0;
	j=strlen(str)-1;
	while(i<=j)
		if(str[i++]!=str[j--])
		{
			flag=0;
			break;
		}
	if(flag)
		printf("True\n");
	else
		printf("False\n");
}

int main()
{
	char str[100];
	gets(str);
	judge(str);
	return 0;
}
