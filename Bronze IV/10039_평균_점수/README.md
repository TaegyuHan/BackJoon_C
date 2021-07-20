# 10039 평균 점수

URL : [https://www.acmicpc.net/problem/10039](https://www.acmicpc.net/problem/10039)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

struct point
{
    int man[5];
};

int main(void)
{

    int i;
    int resultSum=0;
    struct point student;

    for(i=0; i<5; i++)
    {
        scanf("%d", &student.man[i]);
        
        if(student.man[i]<40) //. 보충수업 점수 40
            resultSum += 40;
        else
            resultSum += student.man[i];
    }

    printf("%d", resultSum/5);

	return 0;
}
```

숏 코드

```c
b;main(a){for(;~scanf("%d",&a);)b+=a>40?a/5:8;printf("%d",b);}
```

```c
#include <stdio.h>

int main(void){
    int a[5];
    int sum=0;
    
    for(int i=0; i<5; i++){
        scanf("%d",&a[i]);
        if(a[i]<40){
            a[i]=40;
        }
    }
    
    for(int i=0; i<5; i++){
        sum=sum+a[i];
    }
    printf("%d", sum/5);
   
}
```

```c
#include <stdio.h>

int value(int score);

int main()
{
    int s = 0;//점수를 입력받을 변수
    int sum = 0;//각 점수의 합을 저장할 변수
    int i;//반복문을 위한 변수
    
    for(i = 1; i <= 5; i++)//학생이 5명이므로 5번 반복
    {
        scanf("%d", &s);  //각 점수를 입력받아  
        sum += value(s); //보충학습의 경우를 판별해 sum에 더한다.
    }
    printf("%d", sum / 5);//평균을 출력
}

int value(int score)
{
    int min_s = 40;//최저점수를 40으로 설정한다.
    
    if (score < 40)
        return min_s;
    else
        return score;
}
```

```c
#include <stdlib.h>
#include <stdio.h>
int main(void)
{

    //입력을 받으면 값을 바로 치환해서 각각의 배열에 입력 한다. 

    int i, k, sum = 0;
    int man[5];
    int count;
    int* pa = man;
    count = sizeof(man) / sizeof(man[0]);

    for (i = 0; i < count; i++) {
        scanf("%d", &k);  //30

        if (k < 40) {
            k = 40;
            *(pa + i) = k;
        }
        else if (k > 40 && k % 5 == 0) {
            *(pa + i) = k;
        }
        else if(k % 5 != 0){
            return 0;
        }
        sum += k;
    }
    printf("%d", sum / 5);

}
```