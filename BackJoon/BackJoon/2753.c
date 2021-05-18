
//URL : https://www.acmicpc.net/problem/2753

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2753(void)
{
    int A;

    scanf("%d", &A);

    if (A % 4 == 0 && A % 100 != 0 || A % 400 == 0) {
        printf("%d", 1);
    }
    else {
        printf("%d", 0);
    }

    return 0;
}