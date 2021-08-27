# 2178 미로 탐색

URL : [https://www.acmicpc.net/problem/2178](https://www.acmicpc.net/problem/2178)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define	CHAR_TO_NUM(X) (X) - (48)
#define BOARD_SIZE 101

typedef struct _Data
{
	int width;
	int height;
	char board[BOARD_SIZE][BOARD_SIZE];
	int movements;

	char UpwardState;
	int P_width;
	int P_height;
} Data;

void inputIntData(int* num) { scanf("%d", num); return; }
void inputCharData(char* num) { scanf("%d", num); return; }
void inputStrData(char num[]) { scanf("%s", num); return; }

void ShowBoard(Data* D)
{
	printf("P_width : %d\n", D->P_width);
	printf("P_height : %d\n", D->P_height);
	printf("movements : %d\n", D->movements);

	return;
}

int explore(Data* D)
{
	ShowBoard(D);
	// 목적지 도착하면 반환
	if ((D->width - 1) == D->P_width &&
		(D->height - 1) == D->P_height)
	{
		return D->movements;
	}

	// 처음 출발 0, 0 입력
	if (D->P_width == -1 &&
		D->P_height == -1)
	{
		D->P_width = 0;
		D->P_height = 0;
		(D->movements)++;
		explore(D);
		return D->movements;
	}

	// 오른쪽으로 갈 수 있는지 확인
	if ((D->P_width + 1) < D->width &&
		D->board[D->P_height][D->P_width + 1] == '1')
	{
		(D->P_width)++;
		(D->movements)++;
		D->UpwardState = 0;
		explore(D);
		return D->movements;
	}

	// 아래로 갈 수 있는지 확인
	if ((D->P_height + 1) < D->height &&
		D->board[D->P_height + 1][D->P_width] == '1' &&
		D->UpwardState != 1 )
	{
		(D->P_height)++;
		(D->movements)++;
		D->UpwardState = 0;
		explore(D);
		return D->movements;
	}

	// 위로 갈 수 있는지 확인
	if ((D->P_height - 1) > -1 &&
		D->board[D->P_height - 1][D->P_width] == '1')
	{
		(D->P_height)--;
		(D->movements)++;
		D->UpwardState = 1;
		explore(D);
		return D->movements;
	}

	return 0;
};

int main(void)
{
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	// 데이터 받기
	int i;
	inputIntData(&(D->height)); inputIntData(&(D->width));
	for (i = 0; i < D->height; i++)
		inputStrData(D->board[i]);
	
	// 보드 외부에서 시작
	D->P_height = -1; D->P_width = -1;
	explore(D);

	return 0;
}
```

DFS BFS 공부 필요