# 2231 분해합

URL : [https://www.acmicpc.net/problem/2231](https://www.acmicpc.net/problem/2231)

```c
#include <stdio.h>

#define NUMBER_LEN 8
#define CHAR_TO_NUMBER(X) ((X) - (48))

char Number[NUMBER_LEN];

void InputStringData(char str[])
{
	scanf("%s", str);
}

int StrinLen(char str[])
{
	int i;
	int len=0;

	for (i = 0; str[i] != NULL; i++)
		len++;

	return len;
}

int StringToInt(char str[], int len)
{
	int i;
	int multiTen = 1;
	int sum = 0;

	for (i = len - 1; i >= 0; i--)
	{
		sum += multiTen * CHAR_TO_NUMBER(str[i]);
		multiTen *= 10;
	}

	return sum;
}

int DecompositionSum(int num, int len)
{
	int i;
	int quotaTen = 1;
	int remainTen = 10;
	int sum = num;

	for (i = 0; i < len; i++)
	{
		sum += ((num % remainTen) / quotaTen);
		quotaTen *= 10;
		remainTen *= 10;
	}

	return sum;
}

int main(void)
{
	int i;
	int IntNumber, StrLen;

	InputStringData(Number);

	StrLen = StrinLen(Number);
	IntNumber = StringToInt(Number, StrLen);

	for (i = 0; i < IntNumber; i++)
	{
		if (IntNumber == DecompositionSum(i, StrLen))
		{
			printf("%d", i);
			return 0;
		}
	}

	printf("0");

	return 0;
}
```

숏 코딩

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int atoi(char ch) {
	int n = ch - '0';
	return n;
}

int sum(char* num,int len) {
	int result = num[0] - 1;
	for (int i = 1; i < len; i++) {
		result += 9;
	}
	return result;
}

int solve(int l_num,int r_num) {
	int result = 0, n=l_num, e = 10;
	while (1) {
		result += n % e;
		n /= e;
		if (n == 0)	break;
	}
	result += l_num;
	if (result == r_num)	return 1;
	return 0;
}

int main() {
	char num[8], result[8];
	int l_num, r_num = 0, e = 1, sol = 0;;
	scanf("%s", num);
	int len = strlen(num);
	for (int i = len-1; i >= 0; i--) {
		num[i] = atoi(num[i]);
		r_num += num[i]*e;
		e *= 10;
	}
	l_num = r_num - sum(num, len);
	for (int n = l_num; n <= r_num; n++) {
		if (solve(n, r_num)) {
			printf("%d\n", n);
			sol = 1;
			break;
		}
	}
	if (!sol) printf("0\n");

	return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int n = 0; 
	scanf("%d", &n);
	if (n > 1000000 || n < 1)
	{
		printf("잘못된 입력\n");
		return 0;
	}

	int min = n;
	int num = 0;
	for (int i = 1; i < n; i++)
	{
		num = i;
		int sum = 0;
		while (num > 0)
		{
			sum += num % 10;
			num = num / 10;
		}//각 자릿수의 합

		sum += i;
		//어떤 자연수의 분해합 = 그 자연수 + 그 자연수 각 자리수의 합

		if (sum == n)//어떤 자연수가 n의 생성자일때
		{
			min = i;
			printf("%d", i);
			break;
		}
	}
	if (min == n)//생성자가 없는 경우
	{
		printf("0");
	}

}
```