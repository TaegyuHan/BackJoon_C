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
			}
			else if ((floor - D->board[i][j]) > 0)
			{	// 빼는 시간 1초
				time += (floor - D->board[i][j]);
				InsertBlock += (floor - D->board[i][j]);
			}
		}
	}

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

	// 정답 찾기
	int floor;
	int minimumTime = 0, tmpTime = 0;
	int minimumFloor = 0;

	for (floor = D->lowest; floor <= D->highest; floor++)
	{

		tmpTime = MovingBlockTime(D, floor);

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
		if (minimumTime >= tmpTime)
		{
			minimumFloor = floor;
			minimumTime = tmpTime;
		}
	}

	printf("%d %d", minimumTime, minimumFloor);

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int arr[250000], N, B;

void miner(int high, int* sec);

struct value {
	int over;
	int over_block;
	int pivot;
	int pivot_block;
	int under;
	int under_block;
};

int main()
{
	struct value sec;
	int M, i, range, high, sum = 0, tp;

	scanf("%d %d %d", &N, &M, &B);
	N *= M;
	for (i = 0; i < N; i++)
	{
		scanf("%d", arr + i);
		sum += arr[i];
	}
	high = sum / N;
	range = high / 4;
	if (range < 1) range = 1;
	while (1)
	{
		miner(high, &sec.pivot);
		miner(high + range, &sec.over);
		miner(high - range, &sec.under);
		if (sec.under < sec.pivot && sec.pivot < sec.over)
		{
			high -= range;
		}
		else if (sec.under > sec.pivot && sec.pivot > sec.over)
		{
			high += range;
		}
		else
		{
			if (range > 1)
			{
				range /= 2;
				if (range < 1) range = 1;
			}
			else
			{
				if (sec.pivot_block)
				{
					high -= sec.pivot_block / N;
					range = high / 2;
					if (range < 1) range = 1;
					tp = 0;
					while (1)
					{
						miner(high, &sec.pivot);
						if (sec.pivot_block)
						{
							high -= range;
							if (range > 1)
							{
								range /= 2;
								if (range < 1) range = 1;
							}
							else
							{
								if (tp) break;
							}
						}
						else
						{
							high += range;
							if (range > 1)
							{
								range /= 2;
								if (range < 1) range = 1;
							}
							else
							{
								tp = 1;
							}
						}
					}
					miner(high, &sec.pivot);
					printf("%d %d", sec.pivot, high);
					break;
				}
				else if (sec.pivot == sec.over && !sec.over_block) high += 2;
				else
				{
					printf("%d %d", sec.pivot, high);
					break;
				}
			}
		}
	}

	return 0;
}

void miner(int high, int* sec)
{
	int tp, block = B;
	*sec = 0;
	for (int i = 0; i < N; i++)
	{
		tp = arr[i] - high;
		if (tp > 0)
			*sec += 2 * tp;
		else
			*sec += -tp;

		block += tp;
	}
	if (block < 0) *(sec + 1) = -block;
	else *(sec + 1) = 0;
}
```

```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
int Max(int a, int b) {
	return a > b ? a : b;
}
int Min(int a, int b) {
	return a > b ? b : a;
}
int map[501][501];
int main() {
	int n, m, b;
	scanf("%d %d %d", &n, &m, &b);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	int minland = map[0][0];
	int maxland = map[0][0];
	//벽돌로 만들수있는 땅 높이 구하기. 최소 ~최대
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] > maxland) {
				maxland = map[i][j];
			}
			if (map[i][j] < minland) {
				minland = map[i][j];
			}
		}
	}
	int cnt;
	int max=0,time,copy,alltime=987654321;
	//이제 하나하나 다찾기.
	for (int k = minland; k <= maxland; k++) {
		cnt = b;//카피된 인벤토리에 들어있는 블록
		time = 0;//시간
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == k) {
					continue;
				}
				else if (map[i][j] < k) {//더 작으면 넣어야한다.
					copy = map[i][j];
					while (1) {
						cnt--;//꺼내고
						time += 1;//시간추가
						copy++;//크기증가.
						if (copy == k) {
							break;
						}
					}
				}
				else if (map[i][j] > k) {//더 크면 제거해야한다.
					copy = map[i][j];
					while (1) {
						cnt++;//넣어주고
						time += 2;//시간추가
						copy--;//크기감소
						if (copy == k) {
							break;
						}
					}
				}
			}
		}
		if (cnt>=0) {
			if (alltime > time) {
				alltime = time;
				max = k;
			}
			else if (alltime == time) {
				if (max < k) {
					max = k;
				}
			}
		}
	}
	printf("%d %d", alltime, max);
	return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m, b;
    int **h;
    int **t;
    int total = 0;
    int total_time, min_time, height;
    int minh = 256, maxh;
    
    scanf("%d %d %d", &n, &m, &b);
    
    h = (int **)malloc(sizeof(int *) * n);
    t = (int **)malloc(sizeof(int *) * n);
    
    for(int i=0; i<n; i++)
    {
        h[i] = (int *)malloc(sizeof(int) * m);
        t[i] = (int *)malloc(sizeof(int) * m);
        
        for(int j=0; j<m; j++)
        {
            scanf("%d", &h[i][j]);
            
            total += h[i][j];
            
            if(h[i][j] < minh)
                minh = h[i][j];
        }
    }
    
    total += b;
    
    maxh = total / (n*m);
    
    for(int x=minh; x<=maxh; x++)
    {
        total_time = 0;
        
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(h[i][j] >= x)
                    t[i][j] = 2 * (h[i][j] - x);
                    
                else
                    t[i][j] = x - h[i][j];
                    
                total_time += t[i][j];
            }
        }
        
        if(x == minh)
        {
            height = x;
            min_time = total_time;
        }
        
        if(total_time <= min_time)
        {
            height = x;
            min_time = total_time;
        }
    }
    
    printf("%d %d", min_time, height);
}
```

```c
#include <stdio.h>
#define MAX 500

int CountTime(int N, int M, int level, int(*ground)[500], int *B)
{
	int count = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			int tmp = level - ground[i][j];
			if (tmp > 0)
			{
				count += tmp;
				*B -= tmp;
			}
			else if (tmp < 0)
			{
				count += (-2) * tmp;
				*B += (-tmp);
			}
		}
	}
	return count;
}

int main(void) {
	int N, M, B, defaultB;
	int ground[MAX][MAX];
	int MinTime = 99999999;
	int result = 99999999;

	int lowest = 256, highest = -1;

	scanf("%d %d %d", &N, &M, &defaultB);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++) {
			scanf("%d", &ground[i][j]);
			if (lowest > ground[i][j]) lowest = ground[i][j];
			if (highest < ground[i][j]) highest = ground[i][j];

		}
	}
	for (int level = lowest; level <= highest; level++)
	{
		if (level > 256 || level < 0) return;
		B = defaultB;
		int time = CountTime(N, M, level, ground, &B);
		if (MinTime >= time && B >= 0) {
			MinTime = time;
			result = level;
		}
	}

	printf("%d %d", MinTime, result);

}
```