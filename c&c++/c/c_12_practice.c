#include<stdio.h>

int main()
{
	int n=123456;
	int unitplace=n/1%10;
	int tenplace=n/10%10;
	int hundredplace=n/100%10;
	int thousandplace=n/1000%10;
	printf("%d\n",unitplace);
	printf("%d\n",tenplace);
	printf("%d\n",hundredplace);
	printf("%d\n",thousandplace);
	return 0;
}
