# 1181 단어 정렬 ( 병합정렬로 풀기 )

URL : [https://www.acmicpc.net/problem/1181](https://www.acmicpc.net/problem/1181)

병합정렬 코드

```c
void mergeSort(int data[], int p, int r);
void merge(int data[], int p, int q, int r);
int main() {
     int data[8] = {5,2,4,7,1,3,2,6} , i;
     printf("정렬 전\n");    
     for(i = 0; i < 8; i++) {
         printf("%d ", data[i]);
     }
     mergeSort(data, 0, 7);
     printf("\n정렬 후\n");
     for(i = 0; i < 8; i++) {
         printf("%d ", data[i]);
     }
  return 0;
}
void mergeSort(int data[], int p, int r) {
    int q;
    if(p<r) {
        q = (p+r)/2;
        mergeSort(data, p , q);
        mergeSort(data, q+1, r);
        merge(data, p, q, r);
    }
}
void merge(int data[], int p, int q, int r) {
    int i = p, j = q+1, k = p;
    int tmp[8]; // 새 배열
    while(i<=q && j<=r) {
        if(data[i] <= data[j]) tmp[k++] = data[i++];
        else tmp[k++] = data[j++];
    }
    while(i<=q) tmp[k++] = data[i++];
    while(j<=r) tmp[k++] = data[j++];
    for(int a = p; a<=r; a++) data[a] = tmp[a];
}
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

#define STRING_LEN 51

typedef struct _Node
{
    char str[STRING_LEN];
    int strLen;
} Node;

Node StringList[20001];
Node tmp[20001];

typedef struct _StringNum
{
    int N;
} StringNum;

void InputData(StringNum* SN)
{
    scanf("%d", &SN->N);
}

void merge(int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right)
    {
        if (StringList[i].strLen < StringList[j].strLen)
        {
            tmp[k++] = StringList[i++];
        }
        else if (StringList[i].strLen == StringList[j].strLen)
        {
            int strcheck = strcmp(StringList[i].str, StringList[j].str);
            if (strcheck == 0 || strcheck > 0)
                tmp[k++] = StringList[j++];
            else
                tmp[k++] = StringList[i++];
        }
        else
        {
            tmp[k++] = StringList[j++];
        }
    }

    while (i <= mid)
        tmp[k++] = StringList[i++];

    while (j <= right)
        tmp[k++] = StringList[j++];

    for (int a = left; a <= right; a++)
        StringList[a] = tmp[a];
}

void mergeSort(int left, int right)
{
    int mid;
    if (left < right)
    {
        mid = (left + right) / 2;
        mergeSort(left, mid);
        mergeSort(mid + 1, right);
        merge(left, mid, right);
    }
}

int main()
{
    int i;

    StringNum SN;
    InputData(&SN);

    for (i = 0; i < SN.N; i++)
    {
        scanf("%s", StringList[i].str);
        StringList[i].strLen = strlen(StringList[i].str);
    }

    mergeSort(0, (SN.N - 1));

    char tmp[STRING_LEN] = "11"; // 임의 문자 설정

    for (i = 0; i < SN.N; i++)
    {
        if (strcmp(tmp, StringList[i].str) != 0)
            printf("%s\n", StringList[i].str);
        strcpy(tmp, StringList[i].str);
    }

    return 0;
}
```

숏코딩

```c

```