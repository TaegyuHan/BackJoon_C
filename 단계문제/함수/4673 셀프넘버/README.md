# 4673 셀프 넘버

URL ; [https://www.acmicpc.net/problem/4673](https://www.acmicpc.net/problem/4673)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int SelfNumber(short NumCheck, short SelfNumber);

int main(void)
{
    char BreakNum=0; // 중간 for문 중단 변수
    short i, j; 

    for (i = 1; i <= 10000; i++)
    {
        BreakNum = 0;
        for (j = 1; j <= 10000; j++)
        {
            BreakNum = SelfNumber(j, i); // check 함수 호출
            if (BreakNum==1)
                break;
        }

        if (BreakNum==0)
            printf("%d\n", i);
    }
    return 0;
}

int SelfNumber(short NumCheck, short SelfNumber)
{   // check 함수 
    short result=0;

    char n1 = NumCheck / 10000,     // 10000 자리
        n2 = (NumCheck % 10000) / 1000, // 1000 자리
        n3 = (NumCheck % 1000) / 100,   // 100 자리
        n4 = (NumCheck % 100) / 10,     // 10 자리
        n5 = NumCheck % 10;             // 1 자리;

    // 생성자 확인
    if (NumCheck + n1 + n2 + n3 + n4 + n5 == SelfNumber)
    {
        result = 1;
        return result;
    }

    **return result;**
}
```