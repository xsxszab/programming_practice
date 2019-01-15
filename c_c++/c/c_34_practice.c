#include<stdio.h>
#include<string.h>

int main()
{
	char str[10];
	int num=0;
	gets(str);
	int i=0,j,flag=0;
	j=strlen(str)-1;
	if(str[0]=='-')
	{
		flag=1;
		i++;
	}
	char temp;
	for(;i<=j;i++)
	{
		temp=str[i];
		num+=temp-'0';
		num*=10;
	}
	num/=10;
	if(flag)
		num=-num;
	printf("%d\n",num);
	return 0;
}
