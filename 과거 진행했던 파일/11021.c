
//URL : https://www.acmicpc.net/problem/11021

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon11021(void)
{
    int A, B, C, i;

    scanf("%d", &A);

    for (i = 1; i <= A; i++) {
        scanf("%d %d", &B, &C);
        printf("Case #%d: %d\n", i, B + C);
    }

    return 0;
}