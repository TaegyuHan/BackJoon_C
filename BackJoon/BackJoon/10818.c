
//URL : https://www.acmicpc.net/problem/10818

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon10818(void)
{
    
    int A, B, i, MIN = 1000001, MAX = -1000001;

    scanf("%d", &A);

    for (i=0; i < A; i++)
    {    
        scanf("%d", &B);

        if (B > MAX) MAX = B;
        if (B < MIN) MIN = B;
    }

    printf("%d %d", MIN, MAX);
    return 0;
}