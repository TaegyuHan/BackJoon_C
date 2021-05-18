
//URL : https://www.acmicpc.net/problem/10950

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon10950(void)
{
    int A, B, C;
    scanf("%d", &A);

    for (A; A > 0; A--) {
        scanf("%d %d", &B, &C);
        printf("%d\n", B + C);
    }

    return 0;
}