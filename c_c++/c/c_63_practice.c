#include<stdio.h>
#include<string.h>

#define N 10

void reverse(char str[],char ans[])
{
	int i,j;
	int a;
	j=strlen(str);
	a=j-1;
	while(i<j)
		ans[i++]=str[a--];
	ans[i]='\0';
}

int main()
{
	char str[N];
	char ans[N];
	while(scanf("%s",str)!=EOF)
	{
		reverse(str,ans);
		printf("%s\n",ans);
	}
	return 0;
}
