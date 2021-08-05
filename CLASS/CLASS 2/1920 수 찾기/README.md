# 1920 수 찾기

URL : [https://www.acmicpc.net/problem/1920](https://www.acmicpc.net/problem/1920)

```c
#include <stdio.h>

#define DATA_RANGE 100002

int DATA_COUNT; // N(1 ≤ N ≤ 100,000) 입력 받는 데이터 수
int DATA_SEARCH_COUNT; // M(1 ≤ M ≤ 100,000) 찾는 데이터 수
int data_temp;  //  -2^31 < data_temp < 2^31

int data_list[DATA_RANGE]; // 데이터 리스트
int temp[DATA_RANGE];

void merge(int  data[], int left, int mid, int right)
{
    int i = left,
        j = mid + 1,
        k = left;

    while (i <= mid && j <= right) 
    {
        if (data[i] <= data[j]) temp[k++] = data[i++];
        else temp[k++] = data[j++];
    }
    while (i <= mid) temp[k++] = data[i++];
    while (j <= right) temp[k++] = data[j++];
    for (int a = left; a <= right; a++) data[a] = temp[a];
}

void mergeSort(int  data[], int left, int right)
{
    int mid;
    if (left < right) 
    {
        mid = (left + right) / 2;
        mergeSort(data, left, mid);
        mergeSort(data, mid + 1, right);
        merge(data, left, mid, right);
    }
}

int binSearch(int data[], int n, int key) 
{
    int low, high;
    int mid;

    low = 0;
    high = n - 1;
    while (low <= high) 
    {
        mid = (low + high) / 2;
        if (key == data[mid])            //탐색 성공
            return mid;
        else if (key < data[mid])        //탐색 범위를 아래쪽으로
            high = mid - 1;
        else if (key > data[mid])        //탐색 범위를 위쪽으로
            low = mid + 1;
    }
    return -1;                            //탐색 실패
}

void inputDataCount()
{
    scanf("%d", &DATA_COUNT);
}

void inputDataSearchCount()
{
    scanf("%d", &DATA_SEARCH_COUNT);
}

void inputDataList(int i)
{
    scanf("%d", &data_list[i]);
}

void inputDataTemp()
{
    scanf("%d", &data_temp);
}

void ShowResult(int num)
{
    num = (num == -1) ? 0 : 1;
    printf("%d\n", num);
}

int main()
{
    int i;
    int showTemp;

    // 데이터 삽입
    inputDataCount();
    for (i = 0; i < DATA_COUNT; i++)
    {
        inputDataList(i);
    }

    mergeSort(data_list, 0, DATA_COUNT - 1);

    // 확인 데이터 삽입
    inputDataSearchCount();
    for (i = 0; i < DATA_SEARCH_COUNT; i++)
    {
        inputDataTemp();

        showTemp =  binSearch(data_list, // 데이터
                                DATA_COUNT, // 데이터 수
                                data_temp); // 찾아야 하는 데이터

        ShowResult(showTemp);
    }

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>
//#define max(x,y) (x) < (y) ? (y) : (x)

void QuickSort(int arr[], int left, int right) {
	int L = left, R = right;
	int temp;
	int pivot = arr[(left + right) / 2]; //피봇 위치(중앙)의 값을 받음.
	//데이터 확인 부분.

	//아래의 while문을 통하여 pivot 기준으로 좌, 우 크고 작은 값 나열. = Partition
	while (L <= R) {

		//pivot이 중간 값이고, 비교 대상 arr[L], arr[R]은 pivot과 비교하니 중간 지점을 넘어가면 종료로 볼 수 있음.
		while (arr[L] < pivot) //left부터 증가하며 pivot 이상의 값을 찾음.
			L++;
		while (arr[R] > pivot) //right부터 감소하며 pivot 이하 값을 찾음.
			R--;
		//L, R 모두 최대 pivot 위치까지 이동.

		if (L <= R) { //현재 L이 R이하면. (이유 : L>R 부분은 이미 정리가 된 상태임).
			if (L != R) { //같지 않은 경우만.
				temp = arr[L];
				arr[L] = arr[R];
				arr[R] = temp;
			} //L과 R이 같다면 교환(SWAP)은 필요 없고 한 칸씩 진행만 해주면 됨.
			L++; R--; //그리고 L,R 한 칸 더 진행.
			}
		}
	//조건 확인하여 재귀함수로.
	//데이터 확인 부분.
	if (left < R)
		QuickSort(arr, left, R);
	if (L < right)
		QuickSort(arr, L, right);
}

int binsearch(int data[], int n, int key) {
	int low, high;
	int mid;

	low = 0;
	high = n - 1;
	while (low <= high) {
		mid = (low + high) / 2;
		if (key == data[mid]) {            //탐색 성공
			return mid;
		}
		else if (key < data[mid]) {        //탐색 범위를 아래쪽으로
			high = mid - 1;
		}
		else if (key > data[mid]) {        //탐색 범위를 위쪽으로
			low = mid + 1;
		}
	}
	return -1;                            //탐색 실패
}

int main()
{
	int count;
	scanf("%d", &count);
	getchar();

	int *num_arr = (int*)calloc(count, sizeof(int));
	for (int i = 0; i < count; i++)
		scanf("%d", num_arr + i);
	getchar();

	QuickSort(num_arr, 0, count - 1);
	
	int find_count, find;
	scanf("%d", &find_count);
	for (int i = 0; i < find_count; i++)
	{
		scanf("%d", &find);
		int index = binsearch(num_arr, count, find);
		if (index == -1) printf("0\n");
		else printf("1\n");
	}

	//for (int i = 0; i < count; i++)
	//	printf("%d\n", num_arr[i]);

	return 0;
}
```

```c
#include <stdlib.h>

void sort(int * nIn, int nCnt)
{
	int i, j, nMin, nTemp, nIndex;
	

	for (i = 0; i < nCnt - 1; i++)
	{
		nMin = nIn[i];
		nIndex = -1;
		for (j = i; j < nCnt; j++)
		{
			if (nMin > nIn[j])
			{
				nMin = nIn[j];
				nIndex = j;
			}
		}
		if (nIndex != -1)
		{
			nTemp = nIn[nIndex];
			nIn[nIndex] = nIn[i];
			nIn[i] = nTemp;
		}
	}
}

void recur(int * nIn, int nPivot, int nLeft, int nRight)
{
	int i, j, nTemp;
	int nPivotValue;

	if (nLeft >= nRight)
		return;

	nPivotValue = nIn[nPivot];
	j = nLeft;
	for (i = nLeft + 1; i <= nRight; i++)
	{
		if (nIn[i] < nPivotValue)
		{
			nTemp = nIn[j+1];
			nIn[j + 1] = nIn[i];
			nIn[i] = nTemp;			

			j++;
		}
	}
	nTemp = nIn[j];
	nIn[j] = nIn[nPivot];
	nIn[nPivot] = nTemp;
	nPivot = j;
	recur(nIn, nLeft, nLeft, nPivot - 1);
	recur(nIn, nPivot + 1, nPivot + 1, nRight);

}

void q_sort(int * nIn, int nCnt)
{
	
	recur(nIn, 0, 0, nCnt-1);
}

int binary_search(int * nIn, int nVal, int nLow, int nHigh)
{
	int nMid;
	int nRes;

	nMid = (nHigh + nLow) / 2;

	if (nHigh == nLow)
	{
		if (nIn[nMid] == nVal)
			return 1;
		else
			return 0;
	}

	if (nIn[nMid] == nVal)
	{
		nRes = 1;
	}
	else if (nIn[nMid] > nVal)
	{
		nRes = binary_search(nIn, nVal, nLow, nMid);
	}
	else
	{
		nRes = binary_search(nIn, nVal, nMid+1, nHigh);
	}

	return nRes;
}

int main()
{
	int N, M;
	int i;
	int * N_num;
	int * M_num;
	int nRes;

	scanf("%d", &N);
	N_num = (int *)malloc(N * sizeof(int));

	for (i = 0; i < N; i++)
	{
		scanf("%d", &N_num[i]);
	}

	scanf("%d", &M);
	M_num = (int *)malloc(M * sizeof(int));
	for (i = 0; i < M; i++)
	{
		scanf("%d", &M_num[i]);
	}

	q_sort(N_num, N);

	for (i = 0; i < M; i++)
	{
		nRes = binary_search(N_num, M_num[i], 0, N - 1);
		printf("%d\n", nRes);
	}

	free(N_num);
	free(M_num);

    return 0;
}
```