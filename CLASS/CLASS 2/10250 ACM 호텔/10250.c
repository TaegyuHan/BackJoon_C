#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int cnt;
    int W, H, N;
    scanf("%d", &cnt);

    while(cnt--)
    {
        scanf("%d %d %d", &H, &W, &N);
        int floor=1, number=1;
        for(int i=1; i<N; i++)
        {
            if(floor==H)
            {
                floor=1;
                number++;
                continue;
            }
            floor++;
        }
        printf("%d \n", floor*100 + number);
    }
    return 0;
}
