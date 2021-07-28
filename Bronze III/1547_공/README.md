# 1547 공

URL : [https://www.acmicpc.net/problem/1547](https://www.acmicpc.net/problem/1547)

```c
#include <stdio.h>

#define CUP_NUM 3

typedef struct _Cup
{
	// ( 1 <= LocationChangesNum <= 50 )
	int LocationChangesNum; 

	int CupList[3];

	int AChangePositon;
	int BChangePositon;
} Cup;

void InputLocationChangesNumData(Cup* Cup)
{
	scanf("%d", &Cup->LocationChangesNum);
}

void InputChangePositionData(Cup* Cup)
{
	scanf("%d %d",
		&Cup->AChangePositon,
		&Cup->BChangePositon);
}

int FindIdex(Cup* Cup, int num)
{
	int i;
	for (i = 0; i < CUP_NUM; i++)
		if (Cup->CupList[i] == num)
			return i;
}

void ChangeCupPosition(Cup* Cup)
{
	int AIndex = FindIdex(Cup, Cup->AChangePositon);
	int BIndex = FindIdex(Cup, Cup->BChangePositon);

	int temp = Cup->CupList[AIndex];
	Cup->CupList[AIndex] = Cup->CupList[BIndex];
	Cup->CupList[BIndex] = temp;
}

void ShowBallPosition(Cup* Cup) 
{
	printf("%d", Cup->CupList[0]);
}

void ShowList(Cup* Cup)
{
	int i;
	for (i = 0; i < 3; i++)
		printf("%d ", Cup->CupList[i]);
	printf("\n");
}

int main(void) {

	int i;
	Cup Cup = { 0, {1, 2, 3}, 0, 0 };
	InputLocationChangesNumData(&Cup);

	for (i = 0; i < Cup.LocationChangesNum; i++)
	{
		InputChangePositionData(&Cup);
		ChangeCupPosition(&Cup);
	}

	ShowBallPosition(&Cup);

	return 0;
}
```

숏 코딩

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
   int num;            // 위치를 바꾼 횟수 (0~50)
   int ball_location = 1;   // 공이 들어있는 컵의 위치 (처음 위치 = 1)
   int i;               // for문 카운터
   int change1, change2;   // 서로 바꿀 컵의 위치

   scanf("%d", &num);

   for (i = 0; i < num; i++)
   {
      scanf("%d %d", &change1, &change2);

      if      (change1 == ball_location)   ball_location = change2;
      else if (change2 == ball_location)   ball_location = change1;
   }

   if (ball_location >= 1 && ball_location <= 3)
      printf("%d\n", ball_location);
   else 
      printf("-1");

   return 0;
}
```