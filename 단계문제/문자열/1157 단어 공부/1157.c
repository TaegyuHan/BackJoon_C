#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, result=0, TmpAlpha; //63은 ?
    char StringList[1000001], balpha;
    int j, sum=0, 
        count=0;

    scanf("%s", StringList);

    // 알파벳 소문자 for
    for (i=65; i<91; i++)
    {
        sum=0;
        for(j=0; StringList[j]!='\0'; j++)
        {   // 대소문자 대문자로 변경
            balpha = (StringList[j] > 90) ? StringList[j] - 32 : StringList[j];
            if (balpha==i)
            {
                sum++; // 현재 확인하는 알파벳이면 1 더하기
                TmpAlpha=balpha; // 현재 확인 문자 넣기
            }
        }
        if (sum==0) // 1개도 없으면 
            continue; 
        else if (sum == count) // 가장 큰 값이랑 같으면
            result=63; // ? 표 저장
        else if(sum > count) // 가장 큰 값보다 크면
        {
            result=TmpAlpha; // 알파벳 저장
            count=sum; // 합 저장
        }
    }
    printf("%c \n", result); // 마지막 저장 알파벳 출력
    return 0;
}