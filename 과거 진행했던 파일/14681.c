
//URL : https://www.acmicpc.net/problem/14681

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon14681(void)
{
    int A, B;

    scanf("%d %d", &A, &B);

    if (A > 0 && B > 0) {
        printf("%d",1);
    }
    else if (A > 0 && B < 0) {
        printf("%d", 4);
    }
    else if (A < 0 && B > 0) {
        printf("%d", 2);
    }
    else {
        printf("%d", 3);
    }

    return 0;
}