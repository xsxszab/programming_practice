#include<stdio.h>
#include<memory.h>

char str[8];

long func(int n)
{
	int i;
	long ans=1;
	for(i=1;i<n;i++)
		ans*=10;
	return ans;
}

void transfer(int num)
{
	memset(str,0,sizeof(str));
	int i=0,j=0;
	int temp=num>=0?num:-num;
	if(num<0)
	{
		str[0]='-';
		num=-num;
		i++;
	}
	while(temp)
	{
		temp/=10;
		j++;
	}
	while(j)
		str[i++]=(num/func(j--)%10)+'0';
	str[i]='\0';
}

int main()
{
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		transfer(n);
		printf("%s\n",str);
	}
	return 0;
}
