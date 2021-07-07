# 1193 분수찾기

URL : [https://www.acmicpc.net/problem/1193](https://www.acmicpc.net/problem/1193)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

void DownShowArry(int i, int cnt)
{
    int j;
    for (j=i-1; j>0; j--)
    {   
        if((i-j)==cnt)
            printf("%d/%d\n", j, i-j);
    }
}

void UpShowArry(int i, int cnt)
{
    int j=1;
    for (j=i-1; j>0; j--)
    {
        if((i-j)==cnt)
            printf("%d/%d\n", i-j, j);
    }
}

int main(void)
{
    int i=0, j;
    int InputNum, Sum=0,
        temp;

    scanf("%d", &InputNum);

    // 자연수 합으로 위치 구하기
    for (i; Sum<InputNum; i++)
    {
        Sum += i;
    }

    // 그 행에서의 번째
    temp = InputNum-(Sum-(i-1));

    if(i%2==1)
        // 분자 먼저 시작
        UpShowArry(i, temp);
    else
        // 분모 먼저 시작
        DownShowArry(i, temp);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(){
	int n, cl;
	scanf("%d", &n);
	for(cl=1;n>0;cl++)
		n -= cl;
	if(cl%2)	//odd
		printf("%d/%d\n", cl-1+n, 1-n);
	else		//even
		printf("%d/%d\n", 1-n, cl-1+n);
	return 0;
}
```

```c
#include <stdio.h>

int main()
{
	int n, i;
	scanf("%d", &n);

	for (i = 1; n > i; i++)
	{
		n -= i;
	}

	if (i % 2)
		printf("%d/%d\n", i - n + 1, n);
	else
		printf("%d/%d\n", n, i - n + 1);

	return 0;
}
```

```c
int main()
{
	int A=0,x;
	scanf("%d",&x);
	while(1){
		x-=A+1;
		A++;
		if(x<=0){
			x+=A;
			break;
		}
	}
	if(A%2==0) printf("%d/%d",x,A+1-x);
	else printf("%d/%d",A+1-x,x);

	return 0;
}
```