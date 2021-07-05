
//URL : https://www.acmicpc.net/problem/2439

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2439(void)
{
    int A;

    scanf("%d", &A);

    for (int i = 1; i <= A; i++) {
        for (int k = 1; k <= A - i; k++) {
            printf(" ");
        }
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}