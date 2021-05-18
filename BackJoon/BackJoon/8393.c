
//URL : https://www.acmicpc.net/problem/8393

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon8393(void)
{
    int A, B=0;

    scanf("%d", &A);

    for (A; A > 0; A--) {
        B += A;
    }

    printf("%d", B);

    return 0;
}