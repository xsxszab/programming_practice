void print()
{
	printf("hello world!\n");
}

long calc(int x,int y)
{
	int i;
	long ans=x;
	for(i=0;i<y-1;i++)
		ans*=x;
	return ans;
}
