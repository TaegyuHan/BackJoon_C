
//URL : https://www.acmicpc.net/problem/11022

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon11022(void)
{
    int A, B, C, i;

    scanf("%d", &A);

    for (i = 1; i <= A; i++) {
        scanf("%d %d", &B, &C);
        printf("Case #%d: %d + %d = %d\n", i, B, C, B + C);
    }

    return 0;
}