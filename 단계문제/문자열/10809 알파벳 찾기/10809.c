#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char StringArray[101]; // 입력받을 수를 저장할 배열
    char i, j=0;
    char len = 0;

    scanf("%s", StringArray);

    // 문자열 길이 구하기
    for (i=0; StringArray[i] != '\0'; i++) len++;

    for (i=0; i<26; i++)
    {   
        j=0;
        while(StringArray[j]!=0)
        {
            if((i+97)==StringArray[j])
            {
                printf("%d ", j);
                break;
            }
            j++;
        }
        if(len==j)
            printf("%d ", -1);
    }
    return 0;
}