#include<stdio.h>

int main()
{
	char str[20]={0};
	fgets(str,10,stdin);
	printf("%s\n",str);
	return 0;
}
