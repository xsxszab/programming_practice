#include<stdio.h>

int main()
{
	int num1=123456;
	float num2=123.2345;
	double num3=12333.2345;
	float num4=1111.1111;
	int num5=-1;
	char a='a';
	char str[20]="abcdefgh";
	printf("%d\n",num1);
	printf("%f\n",num2);
	printf("%lf\n",num3);
	printf("%e\n",num3);
	printf("%o\n",num1);
	printf("%#o\n",num1);
	printf("%x\n",num1);
	printf("%X\n",num1);
	printf("%#x\n",num1);
	printf("%c\n",a);
	printf("%d\n",a);
	printf("%s\n",str);
	printf("%2d\n",num1);
	printf("%20d\n",num1);
	printf("%.2f\n",num4);
	printf("%.10f\n",num4);
	printf("%o\n",num5);
	return 0;
}
