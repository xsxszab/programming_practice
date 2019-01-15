#include<stdio.h>

int main()
{
	int n1,n2;
	char str[10];
	scanf("%d%*d%d",&n1,&n2);
	printf("%d\n%d\n",n1,n2);
	printf("----------\n");
	scanf("%s",str);
	printf("%s\n",str);
	printf("----------\n");
	scanf("%3d%4d",&n1,&n2);
	printf("%d\n%d\n",n1,n2);
	printf("----------\n");
	scanf("n1=%d,n2=%d",&n1,&n2);
	printf("%d\n%d\n",n1,n2);
	return 0;
}
