#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, j, k;
    int time=0;
    char InputString[16];
    char NumberList[8][4] = {
        {'A', 'B', 'C'},
        {'D', 'E', 'F'},
        {'G', 'H', 'I'},
        {'J', 'K', 'L'},
        {'M', 'N', 'O'},
        {'P', 'Q', 'R', 'S'},
        {'T', 'U', 'V'},
        {'W', 'X', 'Y', 'Z'},
    };

    scanf("%s", InputString);

    for(i=0; InputString[i]!='\0'; i++)
    {
        for (j=0; j<8; j++) // 배열 8개
        {
            for (k=0; k<4; k++) // 문자 
            {   // 같으면 시간 측정
                if(NumberList[j][k] == InputString[i])
                    time += j + 3;
            }
        }
    }

    printf("%d", time);

    return 0;
}