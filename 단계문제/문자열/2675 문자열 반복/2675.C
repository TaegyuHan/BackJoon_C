#include <stdio.h>

int main(void)
{
    unsigned short i; 
    unsigned char j, k;

    int count, RepeatNum; // 테스트 케이스의 개수, 케이스 반복 횟수
    char StringList[21]; // 문자열

    scanf("%d", &count);

    // 테스트 for 문
    for(i=0; i<count; i++)
    {
        scanf("%d %s", &RepeatNum, StringList);
        j=0;
        // 문자열 for 문
        for(j=0; StringList[j]!='\0'; j++)
        {   
            k=0;
            // 반복 for 문
            for(k=0; k<RepeatNum; k++){
                printf("%c", StringList[j]);
            }
        }
        printf("\n");
    }
    return 0;
}