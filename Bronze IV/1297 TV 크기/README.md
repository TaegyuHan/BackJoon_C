# 1297 TV 크기

URL : [https://www.acmicpc.net/problem/1297](https://www.acmicpc.net/problem/1297)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
#include <math.h>

typedef struct tvSize
{   // H < W || D, H, W는 정수
		int diagonal;   // 5 ≤ D ≤ 1,000
    int hightRatio; // 1 ≤ H ≤ 99
    int widthRatio; // 2 ≤ W ≤ 100
} TvSize;

int main(void)
{
    double x;
    TvSize TS;

    scanf("%d %d %d",
            &TS.diagonal,
            &TS.hightRatio,
            &TS.widthRatio );

    // 피타고라스 정리
    x = sqrt((TS.diagonal*TS.diagonal)) / 
        sqrt((TS.hightRatio*TS.hightRatio + TS.widthRatio*TS.widthRatio));

    // 결과 출력
    printf("%d %d", (int)(x*TS.hightRatio), 
                    (int)(x*TS.widthRatio));

    return 0;
}
```

숏 코딩

```c
#include<stdio.h>
#include<math.h>

int height(double cross, double hp, double wp);
int width(double cross, double hp, double wp);

int main() {
	double cross, hp, wp;
	scanf("%lf %lf %lf", &cross, &hp, &wp);
	printf("%d %d\n", height(cross, hp, wp), width(cross, hp, wp));
	return 0;
}
int height(double cross, double hp, double wp) {
	int a;
	double temp;
	temp = (cross*cross) / (hp*hp + wp*wp);
	a = (int)(hp*sqrt(temp));
	return a;
}
int width(double cross, double hp, double wp) {
	int a;
	double temp;
	temp = (cross*cross) / (hp*hp + wp*wp);
	a = (int)(wp*sqrt(temp));
	return a;
}
```

```c
#include <stdio.h>
#include <math.h>

int main(int argc, const char * argv[])
{
    double daeGak , saeroRatio, garoRatio;
    
    double garo, saero;
    
    int resultA, resultB;
    
    scanf("%lf %lf %lf", &daeGak, &saeroRatio, &garoRatio);
    
    saero = sqrt((daeGak * daeGak)*(saeroRatio*saeroRatio) / (saeroRatio*saeroRatio + garoRatio * garoRatio));
    
    garo = saero*(garoRatio / saeroRatio);
    
    saero = floor(saero);
    garo = floor(garo);
    
    resultA = (int)saero;
    resultB = (int)garo;
    
    printf("%d %d" , resultA, resultB);
    
    
    
    
    
    

}
```

```c
#include <stdio.h>

double square();

int main(void) {
  double a,b,c,answer;
  int d,e;
  scanf("%lf%lf%lf",&a,&b,&c);
  answer = a/square(b*b+c*c);
  d = (int)b*answer;
  e = (int)c*answer;
  printf("%d %d",d,e);
}

double square(double a)
{
  double x =2;

  for(int i = 0;i<100;i++)
  {
    x=(x+(a/x))/2;
  }
  return x;
}
```