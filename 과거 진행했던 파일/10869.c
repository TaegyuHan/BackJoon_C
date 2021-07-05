//URL : https://www.acmicpc.net/problem/10869

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon10869(void)
{
    double num1, num2;

    scanf("%lf %lf", &num1, &num2);

    printf("%.9lf\n", num1 / num2);

    return 0;
}