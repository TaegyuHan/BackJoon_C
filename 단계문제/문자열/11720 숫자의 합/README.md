# 11720 숫자의 합

URL : [https://www.acmicpc.net/problem/11720](https://www.acmicpc.net/problem/11720)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    unsigned char arryLen; // 입력 받을 숫 1이상 100이하
    char NumberArray[101]; // 입력받을 수를 저장할 배열
    int i=0, sum=0; // 결과값 저장

    scanf("%d", &arryLen);
    scanf("%s", NumberArray);

    while(NumberArray[i]!=0)
    {
        sum += ((int)NumberArray[i] - 48);
        i++;
    }

    printf("%d", sum);
    return 0;
}
```

<br>

### 숏코딩

```c
int main() {

	int n, sum = 0;

	scanf("%d", &n);

	while (n--) {
		int a; scanf("%1d", &a); sum += a;
	}

	printf("%d", sum);
}
```

- 처음 받은 정수로 while 문 실행
- %1d 서식문자 사용으로 수 1개씩 받음
- 그리고 더함