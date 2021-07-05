//URL : https://www.acmicpc.net/problem/2588

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2588(void)
{
    int num1, num2;

    scanf("%d %d", &num1, &num2);

    printf("%d\n", num1*(num2 % 10)); // 1의자리
    printf("%d\n", num1*((num2 / 10) % 10)); // 10의 자리
    printf("%d\n", num1*(num2 / 100)); // 100의 자리
    printf("%d\n", num1*num2); // 100의 자리

    return 0;
}