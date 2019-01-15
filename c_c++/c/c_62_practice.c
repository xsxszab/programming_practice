#include<stdio.h>
#include<memory.h>

char str[20];
char ans[20];

int main()
{
	int i=0,j;
	int a,b;
	memset(str,0,sizeof(str));
	memset(ans,0,sizeof(ans));
	gets(str);
	
	while(str[i]!='\0')
	{
		j=i;
		while((str[j]!=' ')&&(str[j]!='\0'))
			j++;
		a=i,b=j-1;
		while(a<j)
			ans[a++]=str[b--];
		i=a;
		ans[i++]=' ';
	}
	ans[i]='\0';
	puts(ans);
	return 0;
}
