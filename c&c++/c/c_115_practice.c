#include<stdio.h>

#define N 10

int len(char str[])
{
	int len=0;
	char *p=str;
	while(*p++)
		len++;
	return len;
}

int main()
{
	char str[N];
	while(scanf("%s",str)!=EOF)
		printf("%d\n-------\n",len(str));
	return 0;
}
