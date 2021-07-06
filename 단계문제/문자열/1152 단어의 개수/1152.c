#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char StrList[1000001], tmp=0;
    unsigned int i, result=0;

    // %[^\n]s > \n 값이 들어오기전까지 문자열 받기
    scanf("%[^\n]s", StrList);

    for(i=0; StrList[i]!='\0'; i++)
    {
        if (tmp==0 && StrList[i]!=32) // 단어 시작
        {
            tmp=1; 
            result+=1; 
        }
        else if (StrList[i]==32) // 띄어쓰기 부분
        {
            tmp=0; 
        }
    }

    printf("%d", result);

    return 0;
}