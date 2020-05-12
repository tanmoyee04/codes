#include<stdio.h>
int a[20][20],visited[20]={0},i,j,front=0,rear=-1,queue[20]={0},n;
int main()
{
	int v;
	printf("enter the number of vertices :\n");
	scanf("%d",&n);
	printf("enter the graph data in the form of matrix :\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	printf("enter the starting vertex :\n");
	scanf("%d",&v);
	bfs(v);
	printf("\n the nodes which are reachable are :\n");
	for(i=0;i<n;i++)
	{
		if(visited[i])
		{
			printf("%d\t",i);
		}
		else
		{
			printf("BFS not possible");
			break;
		}
	}
}
void bfs(int v)
{
	for(i=0;i<n;i++)
	{
		if(a[v][i] && visited[i]==0)
		{
			queue[++rear]=i;
		}
	}
	if(front<=rear)
	{
		visited[queue[front]]=1;
		bfs(queue[front++]);
	}
}
