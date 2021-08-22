# 2630 색종이 만들기

URL : [https://www.acmicpc.net/problem/2630](https://www.acmicpc.net/problem/2630)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PAPER_SIZE 128

void InputIntData(int* num) { scanf("%d", num); }
void InputCharData(char* num) { scanf("%d", num); }

typedef struct _Paper
{
	int inputPageSize;
	int onePaperCnt;
	int zeroPaperCnt;
	char Paper[MAX_PAPER_SIZE][MAX_PAPER_SIZE];
} Paper;

void PageCount(Paper* P, 
	 	int widthStart, int width, 
		int heigthStart, int heigth, int size)
{
	int i=0, j = 0;
	int sum = 0;

	// 종이 확인
	for (i = heigthStart; i < heigth; i++)
	{
		for (j = widthStart; j < width; j++)
		{
			sum += P->Paper[i][j];
		}
	}

	// 흰색 종이 return
	if (sum == size * size)
	{
		(P->onePaperCnt)++;
		return;
	}
	
	// 파란 종이 return
	if (sum == 0)
	{
		(P->zeroPaperCnt)++;
		return;
	}

	// 왼쪽 위
	PageCount(P, 
		widthStart, width - (size / 2), 
		heigthStart, heigth - (size / 2), 
		size / 2);

	// 오른쪽 위
	PageCount(P, 
		widthStart + (size / 2), width,
		heigthStart, heigth - (size / 2), 
		size / 2);

	//// 왼쪽 아래
	PageCount(P, 
		widthStart, width - (size / 2), 
		heigthStart + (size / 2), heigth, 
		size / 2);

	//// 오른쪽 아래
	PageCount(P, 
		widthStart + (size / 2), width,
		heigthStart + (size/ 2), heigth, 
		size / 2);
}

int main(void)
{
	int i, j;

	// 변수 선언
	Paper* Data = (Paper*)malloc(sizeof(Paper));
	memset(Data, 0, sizeof(Paper));

	// 데이터 받기
	InputIntData(&(Data->inputPageSize));
	for (i = 0; i < Data->inputPageSize; i++)
	{
		for (j = 0; j < Data->inputPageSize; j++)
			InputCharData(&(Data->Paper[i][j]));
	}

	// 페이지 개수 카운트
	PageCount(Data, 
		  0, Data->inputPageSize, // 넓이
	          0, Data->inputPageSize, // 높이
		  Data->inputPageSize); // 크기

	// 결과
	printf("%d\n", Data->zeroPaperCnt);
	printf("%d\n", Data->onePaperCnt);

	return 0;
}
```

숏 코딩

```c
int list[129][129];
int blue, white;
void color(int x, int y, int n){
	int i, j, check;
	check = list[x][y];
	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++)
			//재귀 함수에 의해 분리된 사각형이 하나의 색상으로 이루어져있는지 확인하는 부분입니다.
			if (list[x][y] != list[x + i][y + j]){
				check = -1;
				break;
			}
			if (check == -1) break;
	}
	//위의 반복문에 따라 색상의 종이 수를 증가 해줍니다.
	if (check == 1){
		blue++; 
		return; 
	}else if (check == 0){
		white++;
		return;
	}
	// 더이상 자를수 없을 경우 리턴 시켜줍니다. 		
	if (n == 1)   
		return;
	//위의 조건을 만족하지 않을 경우 여러가지 색상이 섞여있는 경우이므로 다음과 같이 재귀를 통해 짤라 줍니다.
	color(x, y, n / 2);
	color(x + n / 2, y, n / 2);
	color(x, y + n / 2, n / 2);
	color(x + n / 2, y + n / 2, n / 2);
}
/* TestCase
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1 
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
*/
int main(){
	
	int n, i, j;

	scanf("%d", &n);
	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++)
			scanf("%d", &list[i][j]);
	}
	color(0, 0, n);// 색상 체크를 위한 재귀함수의 호출입니다.
	printf("%d\n%d\n", white, blue);
    return 0;
}
```

```c
#include<stdio.h>
#include<stdlib.h>
int one = 0;
int zero = 0;

int check( int **a, int start, int end, int jstart) {
    int q = a[start][jstart];
    for (int i = start; i < end; i++) {
        for (int j = jstart; j < jstart + (end - start); j++) {
            if (a[i][j]!= q) {
                return -1;
            }
          
        }
    }
    return q;
}

void d(int **a, int start, int end, int jstart) {
    int q = check(a, start, end,jstart);
    if (q == 1) {
      one++;
    }
    else if (q == 0) {
        zero++;
    }
    else {
        int len = end - start;
        d(a, start, start + len/2, jstart);
        d(a, start,  start +len/2,  jstart + len/2);
        d(a,  start +len/2 , end, jstart);
        d(a,  start +len/2, end ,  jstart +len/2);
    }
}

int main() {
    int qus;

    scanf("%d", &qus);
    int** a = (int**)malloc(qus * sizeof(int*));
    for (int i = 0; i < qus; i++) {
        a[i] = (int*)malloc(sizeof(int) * qus);
    }
    for (int i = 0; i < qus;i++) {
        for (int j = 0; j < qus;j++) {
            scanf("%d",&a[i][j]);
        }
    }
    d(a, 0, qus, 0);
    
  
    printf("%d\n%d", zero, one);
    for (int i = 0; i < qus; i++) {
        free(a[i]);
    }
    free(a);
}
```
