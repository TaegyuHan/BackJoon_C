# 2953 나는 요리사다

URL : [https://www.acmicpc.net/problem/2953](https://www.acmicpc.net/problem/2953)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

#define INPUT_DATA_COUNT 5
#define INPUT_DATA_MAN 4

typedef struct cooker
{
    int man[5];
    int WinnerNumber;
    int WinnerPoint;
} Cooker;

void checkPoint(Cooker * Cooker, int sum, int cookerNumber)
{
    if(Cooker->WinnerPoint < sum)
    {
        Cooker->WinnerNumber = cookerNumber;
        Cooker->WinnerPoint = sum;
    }
}

void inputData(Cooker * Cooker, int cookerNumber)
{
    int i;
    int sum=0;

    for(i=0; i<INPUT_DATA_MAN; i++)
    {
        scanf("%d", &Cooker->man[i]);
        sum += Cooker->man[i];
    }
    checkPoint(Cooker, sum, cookerNumber);
}

int main(void)
{
    int i;
		Cooker Cooker = {
        {0, }, // man
        0,     // WinnerNumber  
        0      // WinnerPoint 
    };

    for(i=0; i<INPUT_DATA_COUNT; i++)
    {
        inputData(&Cooker, i+1);
    }

    printf("%d %d", 
            Cooker.WinnerNumber,
            Cooker.WinnerPoint );

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
//#include <iostream>

#define MAX_SIZE 5

//using namespace std;

int maxIndex(int *arr, int n);
void winner(int (*score)[MAX_SIZE - 1], int *wNum, int *wScore);

int main()
{
    int score[MAX_SIZE][MAX_SIZE - 1];
    int wNum, wScore;

    for (int i = 0; i < MAX_SIZE; i++) {
        for (int j = 0; j <= MAX_SIZE - 2; j++) 
            scanf("%d", &score[i][j]);           
    }
    winner(score, &wNum, &wScore);
    printf("%d %d\n", wNum, wScore);

    return 0;
}

int maxIndex(int *arr, int n)
{
    int max = 0;

    for (int i = 1; i < n; i++) 
        max = arr[i] > arr[max] ? i : max;

    return max;
}

void winner(int (*score)[MAX_SIZE - 1], int *wNum, int *wScore)
{
    int sum[MAX_SIZE];

    for (int i = 0; i < MAX_SIZE; i++) 
        sum[i] = 0;

    for (int i = 0; i < MAX_SIZE; i++) {
        for (int j = 0; j <= MAX_SIZE - 2; j++) 
            sum[i] += score[i][j];
    }    
    *wNum = maxIndex(sum, MAX_SIZE) + 1;
    *wScore = sum[*wNum - 1];
}
```