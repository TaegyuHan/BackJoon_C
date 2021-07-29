# 11721 열 개씩 끊어 출력하기

URL : [https://www.acmicpc.net/problem/11721](https://www.acmicpc.net/problem/11721)

```c
#include <stdio.h>
#define STRING_NUM 10
char STRING[101];

void InputData()
{
	scanf("%s", STRING);
}

void ShowString()
{
	int i;
	int count = 0;
	for (i = 0; STRING[i] != NULL; i++)
	{
		count++;
		printf("%c", STRING[i]);
		if (count == STRING_NUM)
		{
			count = 0;
			printf("\n");
		}
	}
}

int main(void)
{
	InputData();
	ShowString();
	return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main()
{
	char s[100];

	while (scanf("%10s", s) == 1)
		printf("%s\n", s);

	return 0;
}
```

```c
#include <stdio.h>

int main() {

	char str[11];
	
	while (scanf("%10s", str) > 0) {
		printf("%s\n", str);
	}
	
	return 0;
}
```