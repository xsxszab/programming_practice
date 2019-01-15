#include<stdio.h>

union fuck
{
	int a;
	float b;
}exam;

int main()
{
	exam.a=2;
	//wrong: exam=2;
	//傻逼考试题认为这个是对的
	return 0;
}
