# 2869 달팽이는 올라가고 싶다.

URL : [https://www.acmicpc.net/problem/2869](https://www.acmicpc.net/problem/2869)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct _Data
{	// (1 ≤ Down < Up ≤ High ≤ 1,000,000,000)
	int Up; // 낮에 올라가는 높이
	int Down; // 밤에 떨어지는 높이
	int High; // 올라가야 하는 높이
} Data;

void InputIntData(int* num)
{
	scanf("%d", num);
}

int main(void)
{
	Data* D = (Data*)malloc(sizeof(Data));

	InputIntData(&(D->Up));
	InputIntData(&(D->Down));
	InputIntData(&(D->High));

	printf("%d", (D->High - D->Down - 1) / (D->Up - D->Down) + 1);

	free(D);
	return 0;
}
```

숏 코딩

```c
// 2020 11 07
// 달팽이는 올라가고 싶다.

// 하루에 A미터 올라가고 B미터 미끄러지는 달팽이가 있다.
// 달팽이가 V미터인 나무를 올라가려할때
// 며칠이 걸리는지 구하는 프로그램을 작성하라.

// 결국 하루에 A-B미터씩 올라가고
// 마지막날 A미터 혹은 그 보다 적은거리를 올라가면 도착하게 된다
// 수식으로 확인해보면,
// P(A-B) + A >= V인 P를 출력하면 되는거겠지.
// 그르면 P = (V - A) / (A - B) 혹은 이 값에 1을 더 한값이겠지
// 왜냐, 딱 나누어떨어지면 괜찮은데 P는 정수형이니까
// 소수점을 떨어진다 소숫점은 결국, 다음날에 움직여야하는 거리이므로
// 1을 더해야겠지

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int A, B, V;
	int P;
	int i;
	int j;

	scanf("%d %d %d", &A, &B, &V);

	j = (V - A) / (A - B);

	for (i = j; i < V; i++)
	{
		P = (i * (A - B)) + A;
		
		if (P >= V)
		{
			printf("%d\n", (i + 1));
			break;
		}
	}

	return 0;
}
```

```c
/*
 * 알고리즘 설계
 *
 * 1. 올라간 거리(climbMeter), 미끄러진 거리(slipMeter), 막대기 높이(stickMeter)의 값을 입력 받는다.
 * 2. 막대기 높이에서 올라간 거리를 빼서 하루 동안 올라간 거리로 몫을 구한다.
 * 3. 막대기 높이에서 올라간 거리를 빼서 하루 동안 올라간 거리로 나머지를 구한다.
 * 4. 나머지가 0 이상이면 2를 더해주고, 0이면 1을 더해준다.
 * 5. 출력
 */

#include <stdio.h>

int main(void)
{
	int climbMeter;
	int slipMeter;
	int stickMeter;
	int takeDay = 1;
	int numQuotient;
	int numRemainder;
	
	scanf("%d %d %d", &climbMeter, &slipMeter, &stickMeter);
	
	numQuotient = (stickMeter - climbMeter) / (climbMeter - slipMeter);
	numRemainder = (stickMeter - climbMeter) % (climbMeter - slipMeter);
	
	if (numRemainder > 0)
	{
		takeDay = numQuotient + 2;
	}
	else if (numRemainder == 0)
	{
		takeDay = numQuotient + 1;
	}
	
	printf("%d\n", takeDay);
	return 0;
}
```

```c
#include <stdio.h>

int main() {

	int A, B, V;
	int day, almost, answer,howmany;
	
	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &V);

	if (A >= V) { // 만약 올라가야되는 거리가 낮에 달팽이 갈 수 있는 거리와 같다면
		printf("%d", 1); // 하루만에 갈 수 있다.
		return 0;
	}

	day = A - B; // 낮과 밤동안 갈 수 있는 거리
	almost = V - A;// 이 거리까지 오면 무조건 다음날 달팽이는 도착한다.
	if (almost % day) // almost의 거리까지 가는데 걸리는 시간을 구할때 정수값이 안나오면 하루 더 추가
		howmany = (almost / day )+ 1;
	else
		howmany = almost / day;
		
	answer = howmany + 1; // 정상에 도달하려면 하루가 더 걸린다

	printf("%d\n", answer);

	return 0;
}
```