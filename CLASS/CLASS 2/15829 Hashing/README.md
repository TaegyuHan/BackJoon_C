# 15829 Hashing

URL : [https://www.acmicpc.net/problem/15829](https://www.acmicpc.net/problem/15829)

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ALPHABET_TO_NUM(X) ((X) - (96))
#define HASH_NUM 31
#define MOD 1234567891

int STRING_LEN;

void InputIntData(int *num)
{
	scanf("%d", num);
}

void InputStrData(char str[])
{
	scanf("%s", str);
}

void Hash(char str[], int len)
{
	int i;
	long long int hash_value = 0,
				  R = 1;

	for (i = 0; i < len; i++)
	{
		hash_value = (hash_value + ALPHABET_TO_NUM(str[i]) * R) % MOD;
		R = (R * HASH_NUM) % MOD;
	}

	printf("%lld", hash_value);
}

int main(void)
{
	// 문자열 길이 입력
	InputIntData(&STRING_LEN);

	// 문자열 입력받을 배열 생성
	char* alphabetArray = (char*)malloc(sizeof(char) * (STRING_LEN + 1));

	// 문자열 입력
	InputStrData(alphabetArray);

	// 해쉬값 출력
	Hash(alphabetArray, STRING_LEN);

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>

#define MOD 1234567891
#define R   31

typedef unsigned long long UINT64;

UINT64 modPow(int e) {
    int i = 0;
    UINT64 ans = 1;
    
    for (i=0;i<e;i++) {
        ans *= R;
        ans %= MOD;
    }
    
    return ans;
}

UINT64 getIndex(char c) {
    return c - 'a' + 1;
}

int main(void) {
    int l = 0, i = 0;
    UINT64 ans = 0;
    char *p = 0, str[51] = {0, };
    
    p = str;
    
    scanf("%d", &l);
    scanf("%s", str);
    
    while (*p) {
        ans += getIndex(*p) * modPow(i++);
        ans %= MOD;
        p++;
    }
    
    printf("%llu\n", ans);

    return 0;
}
```

```c
#include <stdio.h>

int	main(void)
{
	int		i;
	long long	j;
	int		l;
	long long	sum;
	char	str[50];

	scanf ("%d", &l);
	scanf ("%s", str);

	sum = 0;
	i = 0;
	j = 1;
	while (i < l)
	{
		sum = sum + (((str[i] - 96) * j) % 1234567891);
		j *= 31;
		j %= 1234567891;
		i++;
	}
	printf ("%lld\n", sum % 1234567891);

	return (0);
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
int main() {
	int c;
	scanf("%d", &c);
	char arr[50];
	scanf("%s", arr);
	long long result = 0;

    int i = c-1 ;

	while (i >= 0) {
		result = (result*31 + ((int)arr[i] - 96))%1234567891;
		i=i-1;
	}
	printf("%d", result);
}
```