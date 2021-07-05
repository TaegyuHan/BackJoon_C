
//URL : https://www.acmicpc.net/problem/10871

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon10871(void)
{
    int A, B, C;

    scanf("%d %d", &A, &B);

    for (int i = 0; i < A; i++) {
       scanf("%d", &C);
       if (C < B) {
           printf("%d ", C);
       }
    }

    return 0;
}