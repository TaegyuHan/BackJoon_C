//URL : https://www.acmicpc.net/problem/2588

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int BackJoon2588(void)
{
    int num1, num2;

    scanf("%d %d", &num1, &num2);

    printf("%d\n", num1*(num2 % 10)); // 1���ڸ�
    printf("%d\n", num1*((num2 / 10) % 10)); // 10�� �ڸ�
    printf("%d\n", num1*(num2 / 100)); // 100�� �ڸ�
    printf("%d\n", num1*num2); // 100�� �ڸ�

    return 0;
}