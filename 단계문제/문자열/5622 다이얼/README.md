# 5622 다이얼

URL : [https://www.acmicpc.net/problem/5622](https://www.acmicpc.net/problem/5622)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, j, k;
    int time=0;
    char InputString[16];
    char NumberList[8][4] = {
        {'A', 'B', 'C'},
        {'D', 'E', 'F'},
        {'G', 'H', 'I'},
        {'J', 'K', 'L'},
        {'M', 'N', 'O'},
        {'P', 'Q', 'R', 'S'},
        {'T', 'U', 'V'},
        {'W', 'X', 'Y', 'Z'},
    };

    scanf("%s", InputString);

    for(i=0; InputString[i]!='\0'; i++)
    {
        for (j=0; j<8; j++) // 배열 8개
        {
            for (k=0; k<4; k++) // 문자 
            {   // 같으면 시간 측정
                if(NumberList[j][k] == InputString[i])
                    time += j + 3;
            }
        }
    }

    printf("%d", time);

    return 0;
}
```

<br>

숏 코딩

```c
#include<stdio.h>
int main() {

	char init[16]; // 받는 문자 설정
	gets(init); // input

	int sum = 0; // 결과 저장

	// 받은 문자 for
	for (int i = 0; init[i] != NULL; i++) {
		
		if (init[i] >= 83)init[i]--; // ??
		if (init[i] == 'Z'-1)init[i]--; // ??

		sum += (init[i] - 65) / 3 + 3; // ??
	}

	printf("%d", sum);
}
```

```c
int main() {

	int Eng[27] = { 0,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10 };
	int i,j=0;
	int ans;
	char C[17];

	scanf("%s", C);

	for (i = 0; C[i] != NULL; i++) {
		ans = (C[i] - 'A' + 1);
		j+= Eng[ans];
	}

	printf("%d\n", j);
}
```