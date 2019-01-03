#include<stdio.h>
#include<memory.h>
#include<string.h>

char binary[10];

int transfer(int weight)
{
	int ans=0;
	int i=strlen(binary)-1;
	int temp=1;
	while(i>=0)
	{
		ans+=(binary[i--]-'0')*temp;
		temp*=weight;
	}
	return ans;
}

int main()
{
	scanf("%s",binary);
	printf("%d\n",transfer(2));
	return 0;
}
