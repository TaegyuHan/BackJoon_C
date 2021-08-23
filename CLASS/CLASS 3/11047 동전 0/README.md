# 11047 동전 0

URL : [https://www.acmicpc.net/problem/11047](https://www.acmicpc.net/problem/11047)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_COIN_LEN 10

typedef struct _Data
{
	int coinCount;
	int sumMoney;
	int coinArray[MAX_COIN_LEN];
} Data;

void inputIntData(int* num) { scanf("%d", num); }

void minimumCoinCount(Data* D)
{
	int i, j;
	int sumMoneyTmp = D->sumMoney;
	int resultCoinCount = 0;

	// 가장 값이 큰 코인부터 계산
	for (i = (D->coinCount - 1); i >= 0; i--)
	{
		if (D->coinArray[i] > sumMoneyTmp)
		{	// 코인이 금액의 합보다 큰 경우
			continue;
		}
		else if (D->coinArray[i] == sumMoneyTmp)
		{	// 코인이 금액의 합과 같으면
			sumMoneyTmp -= D->coinArray[i];
			resultCoinCount++;
		}
		else if (D->coinArray[i] < sumMoneyTmp)
		{	// 코인이 금애의 합보다 작은 경우
			for (j = 1; j * D->coinArray[i] <= sumMoneyTmp; j++)
			{	// 코인의 개수를 1개씩 더하면서 빼기
				resultCoinCount++;
			}
			sumMoneyTmp -= (D->coinArray[i] * --j);
		}

		if (sumMoneyTmp <= 0)
			break;
	}

	printf("%d", resultCoinCount);
}

int main(void)
{
	// 변수 설정
	int i;
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	// 데이터 코인개수; 금액;
	inputIntData(&(D->coinCount)); inputIntData(&(D->sumMoney));

	// 코인데이터;
	for (i = 0; i < D->coinCount; i++)
		inputIntData(&(D->coinArray[i]));

	// 결과
	minimumCoinCount(D);

	return 0;
}
```

숏코딩

```c
#include <stdio.h>
int N;
int target;
int money[10];
int count=0;

void get_data(){
//	freopen("Text.txt", "r", stdin);
	scanf("%d", &N);
	scanf("%d", &target);
	for (int i = 0; i < N; i++){
		scanf("%d", &money[i]);
	}
}

int cal_count(int target_money){
	int unit = 0;
	for (int i = 0; i < N; i++){
		if (target_money == money[i]) {
			unit = money[i]; break;
		}
		else if (target_money < money[i]) {
			if (i == 0) return 0;
			unit = money[i - 1]; break; 
		}
		unit = money[i];
	}
	count += target_money / unit;
	target -= unit * (target_money / unit);
	return 1;
}

int main(){
	get_data();
	while (target != 0) {
		if (!cal_count(target)) {
			count = 0; break;
		}
	}
	printf("%d\n", count);
	return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

int main() {

	int i;
	int sum = 0;
	int number_of_coin;
	int object_cash; //we made this cash using coin
	scanf("%d %d", &number_of_coin, &object_cash);
	int * coin = (int *)malloc(sizeof(int)*number_of_coin); //동적할당

	for (i = 0; i < number_of_coin; i++) {
		scanf("%d", &coin[i]);
	}

	while (object_cash != 0) {
		for (i = 0; i < number_of_coin; i++) {
			if (coin[i] > object_cash) {					//i-1에 빼야할 값이 들어있음
				break;
			}
		}
		object_cash -= coin[i - 1];
		sum = sum + 1;
	}

	printf("%d", sum);

	return 0;
}
```