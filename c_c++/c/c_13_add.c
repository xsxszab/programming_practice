#include<stdio.h>
#include<string.h>

int add(char num1[],char num2[],int sum[])
{
	int i,j,len;
	int len1=strlen(num1);
	int len2=strlen(num2);
	int temp[1000]={0};
	len=len1>len2?len1:len2;
	for(i=len1-1,j=0;i>=0;i--,j++)
		sum[j]=num1[i]-'0';
	for(i=len2-1,j=0;i>=0;i--,j++)
		temp[j]=num2[i]-'0';
	for(i=0;i<=len;i++)
	{
		sum[i]+=temp[i];
		if(sum[i]>9)
		{
			sum[i]-=10;
			sum[i+1]++;
		}
	}
	if(sum[len])
		len++;
	return len;
}

int main()
{
	char num1[1000];
	char num2[1000];
	int ans[1000];
	int i,len;
	gets(num1);
	gets(num2);
	len=add(num1,num2,ans);
	for(i=len-1;i>=0;i--)
		printf("%d",ans[i]);
	printf("\n");
	return 0;
}

