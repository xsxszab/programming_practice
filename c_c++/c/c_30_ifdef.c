#include<stdio.h>

#define A
#include"define.h"
#undef A

#define B
#include"define.h"
#define B

int main()
{
	printf("%d\n",A_num);
	printf("%.1f\n",A_weight);
	printf("%d\n",B_num);
	printf("%.1f\n",B_weight);
	return 0;
}
