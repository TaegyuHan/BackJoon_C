
//URL : https://www.acmicpc.net/problem/2739

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2739(void)
{
    int A;

    scanf("%d", &A);

    for (int i=1; i<10; i++) {
        printf("%d * %d = %d\n", A, i, i * A);
    }

    return 0;
}