# 1992 쿼드트리

URL : [https://www.acmicpc.net/problem/1992](https://www.acmicpc.net/problem/1992)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BOARD_SIZE 65
#define DIV_SIZE 2
#define CHAR_TO_NUMBER(X) (X) - (48)

typedef struct _Board
{
	int size;
	char board[MAX_BOARD_SIZE][MAX_BOARD_SIZE];
} Board;

void inputIntData(int* num) { scanf("%d", num); return; }
void inputStrData(char* str) { scanf("%s", str); return; }

void quadTree(Board* B,
	int widthStart, int width,
	int heigthStart, int heigth, int size)
{
	int i, j;
	int sum = 0;

	// 종이 확인
	for (i = heigthStart; i < heigth; i++)
	{
		for (j = widthStart; j < width; j++)
		{
			sum += CHAR_TO_NUMBER(B->board[i][j]);
		}
	}

	// 흑 화면
	if (sum == size * size)
	{
		printf("1");
		return;
	}

	// 백 화면
	if (sum == 0)
	{
		printf("0");
		return;
	}

	printf("(");
	// 왼쪽 위
	quadTree(B,
		widthStart, width - (size / DIV_SIZE),
		heigthStart, heigth - (size / DIV_SIZE),
		size / DIV_SIZE);

	// 오른쪽 위
	quadTree(B,
		widthStart + (size / DIV_SIZE), width,
		heigthStart, heigth - (size / DIV_SIZE),
		size / DIV_SIZE);

	//// 왼쪽 아래
	quadTree(B,
		widthStart, width - (size / DIV_SIZE),
		heigthStart + (size / DIV_SIZE), heigth,
		size / DIV_SIZE);

	//// 오른쪽 아래
	quadTree(B,
		widthStart + (size / DIV_SIZE), width,
		heigthStart + (size / DIV_SIZE), heigth,
		size / DIV_SIZE);
	printf(")");

	return;
}

int main(void)
{
	
	// 변수 설정
	Board* B = (Board*)malloc(sizeof(Board));
	memset(B, 0, sizeof(Board));

	// 데이터 받기
	inputIntData(&(B->size));

	int i;
	for (i = 0; i < B->size; i++)
		inputStrData(B->board[i]);

	// 변경
	quadTree(B, // 데이터
		0, B->size, // 넓이
		0, B->size, // 높이
		B->size); // 크기

	return 0;
}
```

숏 코딩 ( 디버깅 하는 법? )

```c
#include <stdio.h>
#define DEBUG 0
#define MAX_N 70

char bd[MAX_N][MAX_N];
char result[4* MAX_N * MAX_N];
int r_idx;

int divide_conquer(int srow, int scol, int erow, int ecol)
{
#if (DEBUG == 1)
    printf("(%d, %d) - (%d, %d)\n", srow, scol, erow, ecol);
#endif //DEBUG
    
    int i, j;
    char v = bd[srow][scol];
    int different = 0;
    for (i = srow; i <= erow && !different; i++) {
        for (j = scol; j <= ecol && !different; j++) {
            if (bd[i][j] != v) {
                different = 1;
                break;
            }
        }
    }

    if (!different) {
        result[r_idx++] = v;
        
#if (DEBUG == 1)
        printf("result = %s\n", result);
#endif //DEBUG
        
        return 1;
    }

    int terow = (erow - srow + 1) / 2;
    int tecol = (ecol - scol + 1) / 2;
    result[r_idx++] = '(';
    divide_conquer(srow, scol, srow + terow - 1, scol + tecol - 1);
    divide_conquer(srow, scol + tecol, srow + terow - 1, ecol);
    divide_conquer(srow + terow, scol, erow, scol + tecol - 1);
    divide_conquer(srow + terow, scol + tecol, erow, ecol);
    
    result[r_idx++] = ')';
    return 0;
}

int main(void)
{
#if (DEBUG == 1)
    freopen("input_1992.txt", "r", stdin);
    int tc, T;
    scanf("%d", &T);
    for (tc = 0; tc < T; tc++) {
#endif //DEBUG

        int N;
        scanf("%d", &N);

        int i;
        for (i = 1; i <= N; i++) {
            scanf("%s", bd[i] + 1);
        }
        r_idx = 0;
        divide_conquer(1, 1, N, N);
        result[r_idx] = 0;
        printf("%s\n", result);
        
#if (DEBUG == 1)
    }
#endif //DEBUG
    return 0;
}
```

```c
#include <stdio.h>
int a[70][70];
int N;
int chk(int y, int x, int n)
{//시작 y, 시작 x, 범위(한개가아니면 0, 1만있으면 1, 0만있으면 2)
	int i,j,zero=0,one=0;
	for (i = y; i < y + n; i++){
		for (j = x; j < x + n; j++)
		{
			if (a[i][j])one++;
			else zero++;
			if (one&&zero)return 0;
		}
	}
	if (one)return 1;
	else return 2;
}
void DFS(int y, int x, int n)
{
	int tmp;
	tmp = chk(y, x, n);
	if (tmp == 1){ printf("1"); return; }
	else if (tmp == 2){printf("0"); return;}
	else if (!tmp){
		printf("(");
		DFS(y, x, n / 2);
		DFS(y, n / 2 + x, n / 2);
		DFS(n / 2 + y, x, n / 2);
		DFS(n / 2 + y, n / 2 + x, n / 2);
		printf(")");
	}
	return;
}
int main(void)
{
	int i,j,tmp;
	scanf("%d", &N);
	for (i = 1; i <= N; i++){
		for (j = 1; j <= N; j++)scanf("%1d", &a[i][j]);
	}

	tmp = chk(1, 1, N);
	
	if (tmp == 1)printf("1\n");
	else if (tmp == 2)printf("0\n");
	else if (!tmp){
		printf("(");
		DFS(1, 1, N / 2);
		DFS(1, N / 2 + 1, N / 2);
		DFS(N / 2 + 1, 1, N / 2);
		DFS(N / 2 + 1, N / 2 + 1, N / 2);
		printf(")\n");
	}
	return 0;
}
```