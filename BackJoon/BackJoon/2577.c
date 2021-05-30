
//URL : https://www.acmicpc.net/problem/2577

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2577(void)
{
	char arr[10];
	unsigned long int A, B, C;

	scanf("%d %d %d", &A, &B, &C);
	//printf("%d", A * B * C);

	sprintf(arr, "%d", A * B * C);

	printf("%s\n", arr[0]);

	return 0;
}

