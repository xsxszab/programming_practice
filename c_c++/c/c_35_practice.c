#include<stdio.h>

long pow(int n)
{
	int i;
	long ans=1;
	for(i=1;i<n;i++)
		ans*=10;
	return ans;
}

int main()
{
	int num;
	char str[10];
	scanf("%d",&num);
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
		str[i++]=(num/pow(j--)%10)+'0';
	str[i]='\0';
	puts(str);
	return 0;
}
