#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>


int main(void)
{
    char i, j, k,
         tempStr,
         ResultSum = 0;
    char string[101];

    scanf("%d", &i);

    while(i--)
    {
        scanf("%s", string);
        // 첫번째로 도는 문자열
        for (j=0; string[j]!=NULL; j++)
        {
            tempStr = string[j];

            // 처음으로 같은문자가 안나오는 부분 찾기
            for (k=j+1; string[k]!=NULL; k++)
            {
                if(tempStr!=string[k])
                    break;
            }

            // 처음으로 같은문자가 안나오는 부분
            // 부터 같은 문자 나오는지 찾기
            for (k; string[k]!=NULL; k++)
            {
                if(tempStr==string[k])
                {
                    // 나오면 for문 나옴
                    tempStr = -1;
                    break;
                }
            }
            // 나오면 for문 나옴
            if (tempStr==-1)
                break;
        }
        // 더하지 않음
        if (tempStr==-1)
            continue;
        ResultSum++;
    }

    printf("%d", ResultSum);
    return 0;
}
