
//URL : https://www.acmicpc.net/problem/2438

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2438(void)
{
    int A;

    scanf("%d", &A);

    for (int i = 1; i <= A; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}