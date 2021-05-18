
//URL : https://www.acmicpc.net/problem/9498

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon9498(void)
{
    int A;

    scanf("%d", &A);

    if (A > 89) {
        printf("A");
    }
    else if (A > 79) {
        printf("B");
    }
    else if (A > 69) {
        printf("C");
    }
    else if (A > 59) {
        printf("D");
    }
    else {
        printf("F");
    }

    return 0;
}