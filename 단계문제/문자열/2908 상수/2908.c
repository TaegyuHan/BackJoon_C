#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, j;
    char numArray[2][4];

    scanf("%s %s", numArray[1], numArray[2]); // 입력 받기

    for(i=3; i>=0; i--)
    {   
        // 크다면?
        if(numArray[1][i] > numArray[2][i])
        {
            j=1; // 첫번째 수 선택
            break;
        }
        // 작다면?
        if(numArray[1][i] < numArray[2][i])
        {
            j=2; // 두번째 수 선택
            break;
        }
        // 같다면
        if(numArray[1][i] = numArray[2][i])
        {   // 계속 진행
            continue;
        }
    }

    // 반대로 출력
    for(i=2; i>=0; i--)
        printf("%c", numArray[j][i]);

    return 0;
}