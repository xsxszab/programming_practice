#include<stdio.h>
#include<string.h>
#include<memory.h>

char binary[20];

void reverse()
{
	int i=0;
	int j=strlen(binary)-1;
	char temp;
	while(i<j)
	{
		temp=binary[i];
		binary[i++]=binary[j];
		binary[j--]=temp;
	}
}

void transfer(int n)
{
	memset(binary,0,sizeof(binary));
	int i=0;
	while(n)
	{
		binary[i++]=n%2+'0';
		n/=2;
	}
	binary[i]='\0';
	reverse();
}

int main()
{
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		transfer(n);
		puts(binary);
	}
	return 0;
}
