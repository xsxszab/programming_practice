#include<stdio.h>

int main()
{
	int i=1;
	double pi=0,temp=1.0;
	double eps=1e-6;
	while(temp>=eps)
	{
		pi+=temp;
		temp=temp*i/(2*i+1);
		i++;
	}
		pi*=2;
		printf("%.6lf\n",pi);
	return 0;
}
