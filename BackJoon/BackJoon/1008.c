//URL : https://www.acmicpc.net/problem/1008

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon1008(void)
{
    double num1, num2;

    scanf("%lf %lf", &num1, &num2);

    printf("%.9lf\n", num1 / num2);

    return 0;
}