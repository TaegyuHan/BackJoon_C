# 1436 영화감독 숌

URL : [https://www.acmicpc.net/problem/1436](https://www.acmicpc.net/problem/1436)

```c
#include <stdio.h>
#include <math.h>

int INPUT_INT;

void InputIntData()
{
	scanf("%d", &INPUT_INT);
}

void ShowMovieName()
{
	int i;
	int idx = 0;
	int num = 665;

	while (1)
	{
		if (idx == INPUT_INT)
			break;
		
		num++;

	
		for (i = 0; i < 10; i++)
		{
			/*printf("%d \n", (int)pow(10, i));*/

			// 1부터 1000000000 까지 나눠서 
			// 666 찾아낸다. 찾으면 idx 횟수 추가
			if (num / (int)pow(10, i) % 1000 == 666)
			{
				idx++;
				break;
			}
		}
	}
	
	printf("%d", num);
}

int main(void)
{
	InputIntData();
	ShowMovieName();

	return 0;
}
```

숏 코딩

```c
#include<stdio.h>

int main() {

	// 데이터
	int n, num,count = 0,i;
	int start = 666;
	int check;

	// 데이터 입력
	scanf("%d", &n);

	// 입력 받은 수랑 같을때까지 for 문	
	for (i = 666; count != n ; i++) {

		num = i;
		check = 0;
	
		// 10으로 나누면서 666 이 있는지 확인		
		while (num > 0) {
			if (num % 1000 == 666) {
				check = 1;
				break;
			}
			num /= 10;
		}
		if (check) count++;
	   
	}
	printf("%d", i-1);
	
}
```

```c
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main()
{

	// Data
	int n, N=0, i = 0, tmp, cnt = 0;
	scanf("%d", &n);

	// while 문
	while (N != n)
	{
		i++;
		tmp = i;		
		cnt = 0;
		
		while (tmp!=0)
		{
			if (tmp % 10 == 6)
				cnt++;
			else
				cnt = 0;
			if (cnt >= 3)
			{
				N++;
				break;
			}
			tmp /= 10;
		}
		
	}
	printf("%d", i);
}
```