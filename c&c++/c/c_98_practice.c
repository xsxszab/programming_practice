#include<stdio.h>

int main()
{
	printf("%ld\n%ld\n%ld",sizeof(int),sizeof(long int),sizeof(long long int));
	printf("%ld\n%ld\n%ld\n",sizeof(float),sizeof(double),sizeof(long double));
	int a=2;
	printf("%ld\n",sizeof a);
	return 0;
}
