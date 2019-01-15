#include<stdio.h>

enum set
{
	A,B=6,C,D
};

int main()
{
	printf("%d\n%d\n",A,D);
	enum set abcd;
	abcd=B;
	printf("%d\n",abcd	);
	return 0;
}
