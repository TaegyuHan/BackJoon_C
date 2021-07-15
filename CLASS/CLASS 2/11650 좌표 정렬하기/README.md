# 11650 좌표 정렬하기

URL : [https://www.acmicpc.net/problem/11650](https://www.acmicpc.net/problem/11650)

```c
#include <stdio.h>
int array[100001][2] = {0,};
int tmp[100001][2]; // 새 배열

void mergeSort(int data[][2], int p, int r);
void merge(int data[][2], int p, int q, int r);

int main() {

    int i, n;

    scanf("%d", &n);

    for(i=0; i<n; i++)
    {
        scanf("%d %d", &array[i][0], &array[i][1]);
    }

     mergeSort(array, 0, n-1);

     for(i = 0; i < n; i++) {
         printf("%d %d\n", array[i][0], array[i][1]);
     }

  return 0;
}

void mergeSort(int data[][2], int p, int r) {
    int q;

    if(p<r) {
        q = (p+r)/2;
        mergeSort(data, p , q);
        mergeSort(data, q+1, r);
        merge(data, p, q, r);
    }
}

void merge(int data[][2], int p, int q, int r) {
    int i = p, j = q+1, k = p;
    while(i<=q && j<=r) {
        if(data[i][0] < data[j][0])
        {
            tmp[k][0] = data[i][0];
            tmp[k++][1] = data[i++][1];
        } 
        else if(data[i][0] == data[j][0] && data[i][1] < data[j][1])
        {
            tmp[k][0] = data[i][0];
            tmp[k++][1] = data[i++][1];
        }
        else
        {
            tmp[k][0] = data[j][0];
            tmp[k++][1] = data[j++][1];
        } 
    }
    while(i<=q)
    {
        tmp[k][0] = data[i][0];
        tmp[k++][1] = data[i++][1];
    } 
    while(j<=r)
    {
        tmp[k][0] = data[j][0];        
        tmp[k++][1] = data[j++][1];
    } 
    for(int a = p; a<=r; a++)
    {
        data[a][0] = tmp[a][0];        
        data[a][1] = tmp[a][1];
    } 
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int x;
	int y;
}cdn;
void qsort(void *array, size_t n_els, size_t el_size,
					 int compare(const void *, const void *));
int compare(const void *p, const void *q) {
	cdn a = *(cdn *)p;
	cdn b = *(cdn *)q;
	if(a.x>b.x)
		return 1;
	else if(a.x < b.x)
		return -1;
	else if(a.x==b.x) {
		if(a.y > b.y)
			return 1;
		else
			return 0;
	}
}

cdn arr[100001];

int main(void)
{
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++)
		scanf("%d %d", &arr[i].x, &arr[i].y);
	qsort(arr, n, sizeof(cdn), compare);
	for(int i=0; i<n; i++)
		printf("%d %d\n", arr[i].x, arr[i].y);
	return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct cartesian {
   int x;
   int y;
} point;

int compare (const void* m, const void* n);

int main() {
   int N;
   scanf("%d", &N);
   point* points = (point*)malloc(sizeof(point)*N);
   int i;
   for (i = 0; i < N; i++) {
      scanf("%d %d", &points[i].x, &points[i].y);
   }
   qsort(points, N, sizeof(point), compare);
   for (i = 0; i < N; i++) {
      printf("%d %d\n", points[i].x, points[i].y);
   }
   return 0;
}

int compare (const void* m, const void* n) {
   point* a = (point*)m;
   point* b = (point*)n;
   if (a->x > b->x) {
      return 1;
   }
   else if (a->x < b->x) {
      return -1;
   }
   else {
      if (a->y > b->y) {
         return 1;
      }
      else {
         return -1;
      }
   }
}
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct point {
    int x;
    int y;
} point;

int compare_point(const void *a, const void *b);

int main() {
    int n;
    scanf("%d", &n);
    point *points = (point *) malloc(sizeof(point) * n);
    for(int i = 0;i < n;i++) {
        scanf("%d %d", &(points[i].x), &(points[i].y));
    }
    qsort(points, n, sizeof(point), compare_point);
    for(int i = 0;i < n;i++) {
        printf("%d %d\n", points[i].x, points[i].y);
    }
    free(points);
}

int compare_point(const void *a, const void *b) {
    const point *p1 = (point *) a;
    const point *p2 = (point *) b;
    if((p1->x) > (p2->x)) {
        return 1;
    } else if((p1->x) < (p2->x)) {
        return -1;
    } else {
        //p1.x == p2.x
        if((p1->y) > (p2->y)) {
            return 1;
        } else if ((p1->y) < (p2->y)) {
            return -1;
        } else {
            //p1 == p2;
            return 0;
        }
    }
}
```