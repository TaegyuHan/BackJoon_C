
//URL : https://www.acmicpc.net/problem/10952

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon10952(void)
{
    unsigned char A, B;
    scanf("%d %d", &A, &B);

    while ((A + B) > 0)  {
        printf("%d\n", A + B);
        scanf("%d %d", &A, &B);
    }
       
    return 0;
}