
//URL : https://www.acmicpc.net/problem/2562

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2562(void)
{
	int j, A, B=0, i;

	for (i=0; i<9; i++)
	{ 
		scanf("%d", &A);

		if (A > B) 
		{
			B = A;
			j = i + 1;
		}
	}
	printf("%d\n", B);
	printf("%d", j);
}

