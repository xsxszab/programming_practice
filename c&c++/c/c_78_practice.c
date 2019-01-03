#include<stdio.h>

int main()
{
	register int i;
	int ans=0;
	for(i=1;i<=100;i++)
		ans+=i;
	printf("%d\n",ans);
	return 0;
}
