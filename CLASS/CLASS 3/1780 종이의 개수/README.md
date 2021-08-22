# 1780 종이의 개수

URL : [https://www.acmicpc.net/problem/1780](https://www.acmicpc.net/problem/1780)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PAPER_SIZE 2187

void InputIntData(int* num) { scanf("%d", num); }
void InputCharData(char* num) { scanf("%d", num); }

typedef struct _Paper
{
	int inputPageSize;
	int minusPaperCnt;
	int onePaperCnt;
	int zeroPaperCnt;
	char Paper[MAX_PAPER_SIZE][MAX_PAPER_SIZE];
} Paper;

void PageCount(Paper* P, 
			   int widthStart, int width, 
			   int heigthStart, int heigth, int size)
{
	int i=0, j = 0;
	int minusSum = 0;
	int oneSum = 0;
	int zeroSum = 0;

	// 종이 확인
	for (i = heigthStart; i < heigth; i++)
	{
		for (j = widthStart; j < width; j++)
		{
			if (P->Paper[i][j] == -1)
				minusSum++;
				
			if (P->Paper[i][j] == 0)
				zeroSum++;

			if (P->Paper[i][j] == 1)
				oneSum++;
		}
	}

	// -1 종이 return
	if (minusSum == (size * size))
	{
		(P->minusPaperCnt)++;
		return;
	}

	// 0 종이 return
	if (oneSum == size * size)
	{
		(P->onePaperCnt)++;
		return;
	}
	
	// 1 종이 return
	if (zeroSum == size * size)
	{
		(P->zeroPaperCnt)++;
		return;
	}

	// 위 왼쪽
	PageCount(P, 
		widthStart, width - ((size / 3) * 2),
		heigthStart, heigth - ((size / 3) * 2),
		size / 3);

	// 위 중앙
	PageCount(P,
		widthStart + ((size / 3) * 1), width - ((size / 3) * 1),
		heigthStart, heigth - ((size / 3) * 2),
		size / 3);

	// 위 오른쪽
	PageCount(P,
		widthStart + ((size / 3) * 2), width,
		heigthStart, heigth - ((size / 3) * 2),
		size / 3);

	// 중앙 왼쪽
	PageCount(P,
		widthStart, width - ((size / 3) * 2),
		heigthStart + ((size / 3) * 1), heigth - ((size / 3) * 1),
		size / 3);

	// 중앙 중앙
	PageCount(P,
		widthStart + ((size / 3) * 1), width - ((size / 3) * 1),
		heigthStart + ((size / 3) * 1), heigth - ((size / 3) * 1),
		size / 3);

	// 중앙 오른쪽
	PageCount(P,
		widthStart + ((size / 3) * 2), width,
		heigthStart + ((size / 3) * 1), heigth - ((size / 3) * 1),
		size / 3);

	// 아래 왼쪽
	PageCount(P,
		widthStart, width - ((size / 3) * 2),
		heigthStart + ((size / 3) * 2), heigth,
		size / 3);

	// 아래 중앙
	PageCount(P,
		widthStart + ((size / 3) * 1), width - ((size / 3) * 1),
		heigthStart + ((size / 3) * 2), heigth,
		size / 3);

	// 아래 오른쪽
	PageCount(P,
		widthStart + ((size / 3) * 2), width,
		heigthStart + ((size / 3) * 2), heigth,
		size / 3);
}

int main(void)
{
	int i, j;

	// 변수 선언
	Paper* Data = (Paper*)malloc(sizeof(Paper));
	memset(Data, 0, sizeof(Paper));

	// 데이터 받기
	InputIntData(&(Data->inputPageSize));
	for (i = 0; i < Data->inputPageSize; i++)
	{
		for (j = 0; j < Data->inputPageSize; j++)
			InputCharData(&(Data->Paper[i][j]));
	}

	// 페이지 개수 카운트
	PageCount(Data, 
				0, Data->inputPageSize, // 넓이
			    0, Data->inputPageSize, // 높이
				Data->inputPageSize); // 크기

	//// 결과
	printf("%d\n", Data->minusPaperCnt);
	printf("%d\n", Data->zeroPaperCnt);
	printf("%d\n", Data->onePaperCnt);

	return 0;
}
```

숏 코딩

```c
/**
 * @file 03. number of paper.c
 * @author Kdelphinus (delphinus@khu.ac.kr)
 * @brief 
 * @date 2021-07-21 23:01:21
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#include <stdio.h>

int paper[2188][2188];
int minus_one, zero, plus_one;

void DnC(int n, int x, int y)
{
    int flag = 1;

    if (n == 1) // 종이 크기가 1칸이면 종이 개수 추가
    {
        if (paper[y][x] == 1)
            plus_one++;
        else if (paper[y][x] == 0)
            zero++;
        else
            minus_one++;

        return;
    }

    for (int i = y; i < n + y; i++)
    {
        if (flag == 0) // 다른 것이 있으면 반복문 종료
            break;
        for (int j = x; j < n + x; j++)
        {
            if (paper[y][x] != paper[i][j]) // 왼쪽상단과 나머지 범위를 비교해 다른 것이 있으면
            {
                flag = 0; // 다른 것이 있다고 표시하고
                break;    // 반복문 종료
            }
        }
    }

    if (flag) // 다른 것이 없었다면 종이 개수 추가
    {
        if (paper[y][x] == 1)
            plus_one++;
        else if (paper[y][x] == 0)
            zero++;
        else
            minus_one++;

        return;
    }
    else // 다른 것이 있다면
    {
        n /= 3;                       // 9분할
        DnC(n, x, y);                 // 왼쪽 상단
        DnC(n, x + n, y);             // 중앙 상단
        DnC(n, x + 2 * n, y);         // 오른쪽 상단
        DnC(n, x, y + n);             // 왼쪽 중단
        DnC(n, x + n, y + n);         // 중앙 중단
        DnC(n, x + 2 * n, y + n);     // 오른쪽 중단
        DnC(n, x, y + 2 * n);         // 왼쪽 하단
        DnC(n, x + n, y + 2 * n);     // 중앙 하단
        DnC(n, x + 2 * n, y + 2 * n); // 오른쪽 하단
    }
}

int main()
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            scanf("%d", &paper[i][j]);
    }

    DnC(n, 0, 0);
    printf("%d\n%d\n%d", minus_one, zero, plus_one);

    return 0;
}
```

```c
#include <stdio.h>

int arr[2188][2188];
int N;
int zeroNumbers = 0;
int oneNumbers = 0;
int minusOneNumbers = 0;

void getPaper(int startHeight, int endHeight, int startWidth, int endWidth);

int main(){
	scanf("%d", &N);

	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			scanf("%d", &arr[i][j]);
		}
	}

		getPaper(0, N, 0, N);

		printf("%lld\n%lld\n%lld", minusOneNumbers, zeroNumbers, oneNumbers);
}

void getPaper(int startHeight, int endHeight, int startWidth, int endWidth){
	long long oneCount = 0;
	long long zeroCount = 0;
	long long minusCount = 0;
	for(int i = startHeight; i < endHeight; i++){
		for(int j = startWidth; j < endWidth; j++){
			if(arr[i][j] == 1)
				oneCount+=1;
			else if(arr[i][j] == -1)
				minusCount+=1;
			else
				zeroCount+=1;
		}
	}

	int diff = endHeight-startHeight;
	long long rightDiff = diff*diff;
	diff = diff/3;

	if(oneCount == rightDiff){
		oneNumbers+=1; 
		return ;
	}else if(zeroCount == rightDiff){
		zeroNumbers+=1;
		return;
	}else if(minusCount == rightDiff){
		minusOneNumbers+=1;
		return;
	}

	getPaper(startHeight, startHeight+diff, startWidth, startWidth+diff);	
	getPaper(startHeight, startHeight+diff, startWidth+diff, endWidth-diff);	
	getPaper(startHeight, startHeight+diff, endWidth-diff, endWidth);	
	getPaper(startHeight+diff, endHeight-diff, startWidth, startWidth+diff);	
	getPaper(startHeight+diff, endHeight-diff , startWidth+diff, endWidth-diff);	
	getPaper(startHeight+diff, endHeight-diff , endWidth-diff, endWidth);	
	getPaper(endHeight-diff, endHeight, startWidth, startWidth+diff);	
	getPaper(endHeight-diff, endHeight, startWidth+diff, endWidth-diff);	
	getPaper(endHeight-diff, endHeight, endWidth-diff, endWidth);	
}
```