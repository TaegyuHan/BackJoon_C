# 18111 마인크래프트

URL : [https://www.acmicpc.net/problem/18111](https://www.acmicpc.net/problem/18111)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BOARD_SIZE 5000

typedef struct _Data
{
	int width;
	int height;

	int highest;
	int lowest;
	int inventory;

	int board[BOARD_SIZE][BOARD_SIZE];

} Data;

void inputIntData(int* num) { scanf("%d", num); return; }

void checkHighest(Data* D, int i , int j)
{
	D->highest = (D->board[i][j] > D->highest) ? 
				  D->board[i][j] : D->highest;
	return;
}

void checkLowest(Data* D, int i, int j)
{
	D->lowest = (D->board[i][j] < D->lowest) ?
				 D->board[i][j] : D->lowest;
	return;
}

int MovingBlockTime(Data* D, int floor)
{
	int i, j;
	int time = 0;
	int SubtractBlocks = 0;
	int InsertBlock = 0;

	// board 돌기
	for (i = 0; i < D->height; i++)
	{
		for (j = 0; j < D->width; j++)
		{
			// 블록 추가 삭제 판별
			if ((floor - D->board[i][j]) < 0)
			{	// 빼는 시간 2초
				time += -1 * (floor - D->board[i][j]) * 2;
				SubtractBlocks -= (floor - D->board[i][j]);
				printf("%d ", floor - D->board[i][j]);
			}
			else if ((floor - D->board[i][j]) > 0)
			{	// 빼는 시간 1초
				time += (floor - D->board[i][j]);
				InsertBlock += (floor - D->board[i][j]);
				printf("%d ", floor - D->board[i][j]);
			}
		}
		printf("\n");
	}
	printf("time : %d\n", time);
	printf("D->inventory : %d\n", D->inventory);
	printf("SubtractBlocks : %d\n", SubtractBlocks);
	printf("InsertBlock : %d\n", InsertBlock);

	// 이벤토리양보다 더 많이 삽입 하는 경우
	if (InsertBlock > SubtractBlocks + D->inventory)
		return -1;
	else
		return time;
}

int main(void)
{
	// 변수 설정
	int i, j;
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	// 데이터 삽입
	inputIntData(&(D->height)); inputIntData(&(D->width)); inputIntData(&(D->inventory));

	for (i = 0; i < D->height; i++)
	{
		for (j = 0; j < D->width; j++)
		{
			inputIntData(&(D->board[i][j]));

			// 첫번째 input값 등록
			if (i == 0 && j == 0)
			{
				D->lowest = D->board[i][j];
				D->highest = D->board[i][j];
			}

			// 최대, 최소 높이 구하기
			checkHighest(D, i, j);
			checkLowest(D, i, j);
		}
	}

	printf("D->inventory : %d\n", D->inventory);
	printf("D->lowest : %d\n", D->lowest);
	printf("D->highest : %d\n", D->highest);

	int floor;
	int minimumTime = 0, tmpTime = 0;
	int minimumFloor = 0;

	for (floor = D->lowest; floor <= D->highest; floor++)
	{
		printf("floor : %d\n", floor);

		tmpTime = MovingBlockTime(D, floor);

		printf("tmpTime %d\n", tmpTime);

		// 블록 양이 부족한 경우
		if (tmpTime == -1)
			continue;

		// 처음 시작
		if (minimumTime == 0)
		{
			minimumFloor = floor;
			minimumTime = tmpTime;
			continue;
		}
		
		// 두번째 시작 적은 시간 찾기
		if (minimumTime > tmpTime)
		{
			minimumFloor = floor;
			minimumTime = tmpTime;
		}
	}

	printf("%d %d", minimumTime, minimumFloor);

	return 0;
}
```

반례 버그 수정 필요