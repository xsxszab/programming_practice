#include<stdio.h>
#include<memory.h>
#include<string.h>

char octal[10];

void reverse()
{
	int i=0;
	int j=strlen(octal)-1;
	char temp;
	while(i<j)
	{
		temp=octal[i];
		octal[i++]=octal[j];
		octal[j--]=temp;
	}
}

void transfer(int n)
{
	memset(octal,0,sizeof(octal));
	int i=0;
	while(n)
	{
		octal[i++]=n%8+'0';
		n/=8;
	}
	octal[i]='\0';
	reverse();
}

int main()
{
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		transfer(n);
		printf("%s\n",octal);
	}
	return 0;
}
