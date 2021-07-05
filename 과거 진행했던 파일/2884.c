
//URL : https://www.acmicpc.net/problem/2884

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2884(void)
{
    int A, B;

    scanf("%d %d", &A, &B);

    if ( B - 45 < 0 ) {
        if (A != 0) {
            printf("%d %d", A - 1, B + 15);
        }
        else {
            printf("%d %d", 23, B + 15);
        }
    }
    else {
        printf("%d %d", A, B - 45);
    }
    return 0;
}