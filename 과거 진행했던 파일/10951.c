
//URL : https://www.acmicpc.net/problem/10951

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon10951(void)
{
    unsigned char A, B;

    while (scanf("%d %d", &A, &B) != EOF) {
        printf("%d\n", A + B);
    }

    return 0;
}