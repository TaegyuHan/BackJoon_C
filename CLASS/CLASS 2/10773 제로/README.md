# 10773 제로

URL : [https://www.acmicpc.net/problem/10773](https://www.acmicpc.net/problem/10773)

```c
#include <stdio.h>

int checkZero(int arr[], int sum, int i)
{
    if(arr[i]==0)
    {
        checkZero(arr, sum, i-1);
    }
    else
    {
        sum -= arr[i];
        arr[i] = 0;
        return sum;
    }
}

int main() {

    int i, n, j=0, sum=0;
    int arr[100001];

    scanf("%d", &n);

    for(i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
        if(arr[i]==0)
        {   
            sum = checkZero(arr, sum, i-1);
        }
        else 
        {
            sum += arr[i];
        }
    }

    printf("%d", sum);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int arr[1000001],cnt;

int main(){
	
	int n;
	scanf("%d",&n);
	
	for(;n--;){
		int num;
		scanf("%d",&num);
		
		if(num==0){
			if(cnt!=0)cnt--;
		}
		else{
			arr[cnt++]=num;
		}
		
	}
	int sum=0;
	for(int i=0;i<cnt;i++)
		sum+=arr[i];
	
	printf("%d",sum);
	
	
	return 0;			
}
```

```c
#include <stdio.h>
int main(void)
{
	int k[100000]; int num, n, i, cnt=-1;
	long long result=0;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &num);
		if (num != 0) { cnt++; k[cnt] = num;  }
		else cnt--;
	}
	for (i = 0; i < cnt + 1; i++)
	{
		result += k[i];
	}
	printf("%d", result);
	return 0;
}
```

```c
#include <stdio.h>
#define max 100000

int arr[max];

int main() {
	int k,num;
	int total = 0;
	scanf("%d ", &k);

	int i = 0;
	int j = 0;
	for (i = 0; i < k; i++) {
		scanf("%d", &num);
		if (num == 0) {
			total -= arr[--j];
		}
		else {
			arr[j++] = num;
			total += num;
		}
	}

	printf("%d", total);
	return 0;
}
```