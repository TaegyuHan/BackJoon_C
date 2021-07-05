
//URL : https://www.acmicpc.net/problem/1330

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon1330(void)
{
    int A, B;

    scanf("%d %d", &A, &B);

    if (A > B) {
        printf(">");
    }
    else if (A < B) {
        printf("<");
    }
    else {
        printf("==");
    }

    return 0;
}