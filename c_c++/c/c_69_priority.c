#include<stdio.h>

struct A
{
	int a;
	int b;
};

struct B
{
	char a;
	int b;
};

struct C_1
{
	int a;
	char b;
	int c;
};

struct C_2
{
	int a;
	int b;
	char c;
};

int main()
{
	printf("%ld\n",sizeof(struct A));
	printf("%ld\n",sizeof(struct B));
	printf("%ld\n",sizeof(struct C_1));
	printf("%ld\n",sizeof(struct C_2));
	return 0;
}
