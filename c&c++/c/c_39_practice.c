#include<stdio.h>

int len(const char *str)
{
	int len=0;
	while(str[len++]!='\0')
		NULL;
	return len-1;
}

int main()
{
	char str[20];
	scanf("%s",str);
	printf("%d\n",len(str));
	return 0;
}
