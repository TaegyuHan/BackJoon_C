# 3053 택시 기하학

URL : [https://www.acmicpc.net/problem/3053](https://www.acmicpc.net/problem/3053)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

#define PI 3.1415926535897932384626433

typedef struct radius
{
    int N;
} Radius;

void result(Radius Radius)
{
    printf("%.6f\n", Radius.N*Radius.N*PI);
    printf("%.6f\n", (double)Radius.N*Radius.N*2.0);
}

int main(void)
{
    Radius Radius;

    scanf("%d", &Radius);
    result(Radius);

    return 0;
}
```

숏 코딩

```c
void solve(int test_num){
	double R;
	
	scanf("%lf", &R);
	
	printf("%.5f\n", R*R*M_PI);
	printf("%.5f\n", R*R*2.0);
}

int main(){

  	solve(0);

	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int radius;
	double pi = 3.141592653589793238462643383279502;
	scanf("%d", &radius);

	double answer1 = radius * radius * pi;
	double answer2 = radius * radius * 2;
	printf("%.6f\n", answer1);
	printf("%.6f", answer2);

	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define PI 3.14159265358979323846

int r;

double Euclide(int n) {
	double S = (double)(n*n)*PI;
	return S;
}

double Taxi(int n) {
	double S = (double)(n*n * 2);
	return S;
}

int main() {
	scanf("%d", &r);
	printf("%.6f\n", Euclide(r));
	printf("%.6f\n", Taxi(r));
	return 0;
}
```