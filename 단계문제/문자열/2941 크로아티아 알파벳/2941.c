#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char string[101]; // 문자열 저장 배열
    char i;
    char ResultSum=0; // 결과 저장

    scanf("%s", string);

    // 문자열 확인
    for(i=0; string[i]!=NULL; i++)
    {
        ResultSum++;
        if(string[i]=='=' && string[i-1]=='c') // c=
            ResultSum -= 1;
        else if(string[i]=='-' && string[i-1]=='c') // c-
            ResultSum -= 1;
        else if(string[i]=='=' && string[i-1]=='z' && string[i-2]=='d') // dz=
            ResultSum -= 2;
        else if(string[i]=='-' && string[i-1]=='d') // d-
            ResultSum -= 1;
        else if(string[i]=='j' && string[i-1]=='l') // lj
            ResultSum -= 1;
        else if(string[i]=='j' && string[i-1]=='n') // nj
            ResultSum -= 1;
        else if(string[i]=='=' && string[i-1]=='s') // s=
            ResultSum -= 1;
        else if(string[i]=='=' && string[i-1]=='z') // z=
            ResultSum -= 1;
    }

    printf("%d", ResultSum);

    return 0;
}