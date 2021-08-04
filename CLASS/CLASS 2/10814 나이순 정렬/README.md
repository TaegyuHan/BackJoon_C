# 10814 나이순 정렬

URL : [https://www.acmicpc.net/problem/10814](https://www.acmicpc.net/problem/10814)

```c
#include <stdio.h>

#define NAME_LEN 101
#define PEOPLE_LEN 100001

int DATA_COUNT;

typedef struct _ManInfo
{
    unsigned char age;
    char name[NAME_LEN];

} ManInfo;

ManInfo member[PEOPLE_LEN];
ManInfo temp[PEOPLE_LEN];

void merge(ManInfo data[], int left, int mid, int right)
{
    int i = left,
        j = mid + 1,
        k = left;

    while (i <= mid && j <= right) 
    {
        if (data[i].age <= data[j].age) temp[k++] = data[i++];
        else temp[k++] = data[j++];
    }
    while (i <= mid) temp[k++] = data[i++];
    while (j <= right) temp[k++] = data[j++];
    for (int a = left; a <= right; a++) data[a] = temp[a];
}

void mergeSort(ManInfo data[], int left, int right)
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

void INPUT_DATA_COUNT()
{
    scanf("%d", &DATA_COUNT);
};

void insertMemberInfo(int i)
{
    scanf("%d %s", 
            &member[i].age,
             member[i].name );
}

void ShowMemberInfo(int i)
{
    printf("%d %s\n",
        member[i].age,
        member[i].name);
}

int main()
{
    int i;
    INPUT_DATA_COUNT();

    // 데이터 입력 받기
    for (i = 0; i < DATA_COUNT; i++)
    {
        insertMemberInfo(i);
    }

    mergeSort(member, 0, DATA_COUNT - 1);

    for (i = 0; i < DATA_COUNT; i++)
    {
        ShowMemberInfo(i);
    }

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

typedef struct s_user{
  int age;
  char name[101];
}              t_user;

void change(t_user *a, t_user *b)
{
  t_user *temp;
  temp = a;
  a = b;
  b = temp;
}

int main(void) {
  int n;
  scanf("%d", &n);
  t_user user[n];
  int i = 0;
  int min;
  int max; 
  while (i < n)
  {
    scanf("%d %s", &user[i].age, user[i].name);
    if (i != 0)
    {
      if (min > user[i].age)
        min = user[i].age;
      if (max < user[i].age)
        max = user[i].age;
    }
    else
      max = min = user[i].age;
    i++;
  }
  while (min <= max)
  {
    i = 0;
    while (i < n)
    {
      if(min == user[i].age)
        printf("%d %s\n", user[i].age, user[i].name);
      i++;
    }
    min++;
  }
  return 0;
}
```

```c
long int m, n, count;

struct id 
{
	int a, num;
	char name[110];
};

struct id ids[100001];
long int num;
int com(const void *a, const void *b);

int main(void)
{
	long int i;
	scanf("%ld", &num);
	for (i = 0; i < num; i++)
	{
		scanf("%d %s", &ids[i].a, ids[i].name);
		ids[i].num = i;
	}
	qsort(ids, num, sizeof(struct id), com);
	for (i = 0; i < num; i++)
		printf("%d %s\n", ids[i].a, ids[i].name);
	return 0;
}

int com(const void *a, const void *b)
{
	struct id m, n;
	m = *(struct id *)a, n = *(struct id *)b;
	if (m.a > n.a)
		return 1;
	if (m.a < n.a)
		return -1;
	else
	{
		if (m.num > n.num)
			return 1;
		if (m.num < n.num)
			return -1;
		else
			return 0;
	}
}
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct _Member {
	int no;
	int age;
	char name[100 + 1];
} Member;

int compare_member(void* a, void* b)
{
	Member* member_a = (Member*)a;
	Member* member_b = (Member*)b;
	if (member_a->age == member_b->age) {
		return member_a->no - member_b->no;
	}
	return member_a->age - member_b->age;
}

int main()
{
	int n;
	int i;
	Member* members;

	scanf("%d", &n);
	members = (Member*)malloc(n * sizeof(Member));

	for (i = 0; i < n; i++) {
		members[i].no = i;
		scanf("%d %s", &members[i].age, members[i].name);
	}

	qsort(members, n, sizeof(Member), compare_member);

	for (i = 0; i < n; i++) {
		printf("%d %s\n", members[i].age, members[i].name);
	}

	return 0;
}
```