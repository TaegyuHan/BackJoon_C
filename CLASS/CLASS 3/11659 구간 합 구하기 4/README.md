# 11659 구간 합 구하기 4

URL : [https://www.acmicpc.net/problem/11659](https://www.acmicpc.net/problem/11659)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_LEN 100001

typedef struct _Data
{
	int numberArrayLen;
	int testLen;
	int testIndexF;
	int testIndexB;
	int Array[ARRAY_LEN];
} Data;

void InputIntData(int* num) { scanf("%d", num); return; }

void resultPrint(Data* D, int start, int end)
{
	// resul
	if (start == 1)
		printf("%d\n", D->Array[end - 1]);
	else
		printf("%d\n", D->Array[end - 1] - D->Array[start - 2]);
};

int main(void)
{
	// 변수 설정
	Data* data = (Data*)malloc(sizeof(Data));
	memset(data, 0, sizeof(Data));

	InputIntData(&(data->numberArrayLen)); InputIntData(&(data->testLen));

	// 데이터 입력
	int i;
	for (i = 0; i < data->numberArrayLen; i++)
	{
		if (i == 0)
		{
			// 첫번째 수
			// 그냥 insert
			InputIntData(&(data->Array[i]));
			continue;
		}
		else
		{
			// 두번째 수 전에 있는 데이터 합치고 입력
			InputIntData(&(data->Array[i]));
			data->Array[i] = data->Array[i] + data->Array[i - 1];
		}
	}

	// TEST
	for (i = 0; i < data->testLen; i++)
	{
		InputIntData(&(data->testIndexF)); InputIntData(&(data->testIndexB));

		// 결과
		resultPrint(data, data->testIndexF, data->testIndexB);
	}

	free(data);
	return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int N, M;
int arr[100001];

int main(void)
{
	scanf("%d %d", &N, &M);

	for (int i = 1; i <= N; i++) {
		int temp = 0;
		scanf("%d", &temp);
		arr[i] = temp + arr[i - 1];
	}

	for (int i = 0; i < M; i++) {
		int s, e;
		scanf("%d %d", &s, &e);
		printf("%d\n", arr[e] - arr[s-1]);
	}

	return 0;
}
```

```c
int N, M;
int num[100003];
long long sum_result[100003];

int main(void)
{
	int i, start, end;

	scanf("%d %d", &N, &M);

	for (i = 1; i <= N; i++)
		scanf("%d", &num[i]);

	for (i = 1; i <= N; i++)
		sum_result[i] = sum_result[i - 1] + num[i];
		
	for (int tc = 1; tc <= M; tc++)
	{
		scanf("%d %d", &start, &end);
		printf("%lld\n", sum_result[end] - sum_result[start-1]);
	}

	return 0;
}
```