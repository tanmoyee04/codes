#include<stdio.h>
#include<limits.h>        //for INT_MAX 

void main()
{
	int arr[]={20,30,50,10,5};
	int n=sizeof(arr)/sizeof(arr[0]);
	printf("the minimum number of multiplications required are : %d",matrixchainmultiplication(arr,1,n-1));
}
int matrixchainmultiplication(int p[],int i,int j)
{
	int k,count,min;
	min=INT_MAX;         //it is a macro that specifies that an integer variable cannot store any value beyond this limit.
	for(k=i;k<j;k++)
	{
		count= matrixchainmultiplication(p,i,k)+matrixchainmultiplication(p,k+1,j)+p[i-1]*p[k]*p[j];
		if(count<min)
		{
			min=count;
		}
	}
	return min;
}

