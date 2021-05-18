
//URL : https://www.acmicpc.net/problem/1110

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon1110(void)
{
    unsigned char A, B, C, i;

    scanf("%d", &A);

    B = C = A;
    i = 1;

    while (1)
    {
        B = C;
        C = ((B % 10) * 10) + (((B % 10) + (B / 10)) % 10);
        if (C==A)
        {
            printf("%d", i);
            break;
        }
        i++;
    }
    return 0;
}