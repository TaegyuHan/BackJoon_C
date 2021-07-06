#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    unsigned char arryLen; // 입력 받을 숫 1이상 100이하
    char NumberArray[101]; // 입력받을 수를 저장할 배열
    int i=0, sum=0; // 결과값 저장

    scanf("%d", &arryLen);
    scanf("%s", NumberArray);

    while(NumberArray[i]!=0)
    {
        sum += ((int)NumberArray[i] - 48);
        i++;
    }

    printf("%d", sum);
    return 0;
}