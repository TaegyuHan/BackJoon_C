# 1018 체스판 다시 칠하기

URL : [https://www.acmicpc.net/problem/1018](https://www.acmicpc.net/problem/1018)

```c
#include <stdio.h>
char Board[50][50];

void WCheckBoard(int x, int y, int * ResultSum)
{
    int i, j, cnt=0;
    int widthStart = 0+x;
    int widthEnd = widthStart+8;
    int heightStart = 0+y;
    int heightEnd = heightStart+8;
    int sum=0;

    for(i=widthStart; i<widthEnd; i++)
    {
        if(i%2==0)
        {
            // > 방향으로 확인
            for(j=heightStart; j<heightEnd; j++)
            {
                // printf("%c", Board[i][j]);
                if(cnt%2==0 && Board[i][j]=='W')
                {
                    cnt++;
                    continue;
                }
                else if(cnt%2==0 && Board[i][j]=='B')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='W')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='B')
                {
                    cnt++;
                    continue;
                }
            }
        }
        else
        {
            // < 방향으로 확인
            for(j=(heightEnd-1); j>=heightStart; j--)
            {
                // printf("%c", Board[i][j]);
                if(cnt%2==0 && Board[i][j]=='W')
                {
                    cnt++;
                    continue;
                }
                else if(cnt%2==0 && Board[i][j]=='B')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='W')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='B')
                {
                    cnt++;
                    continue;
                }
            }
        }
    }

    // printf("\nx : %d, y : %d, sum : %d\n", x, y, sum);
    * ResultSum = sum;
}

void BCheckBoard(int x, int y, int * ResultSum)
{
    int i, j, cnt=0;
    int widthStart = 0+x;
    int widthEnd = widthStart+8;
    int heightStart = 0+y;
    int heightEnd = heightStart+8;
    int sum=0;

    for(i=widthStart; i<widthEnd; i++)
    {
        if(i%2==0)
        {
            // > 방향으로 확인
            for(j=heightStart; j<heightEnd; j++)
            {
                // printf("%d %d\n", i, j);
                // printf("%c", Board[i][j]);
                if(cnt%2==0 && Board[i][j]=='B')
                {
                    cnt++;
                    continue;
                }
                else if(cnt%2==0 && Board[i][j]=='W')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='B')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='W')
                {
                    cnt++;
                    continue;
                }
            }
        }
        else
        {
            // < 방향으로 확인
            for(j=(heightEnd-1); j>=heightStart; j--)
            {
                // printf("%d %d\n", i, j);
                // printf("%c", Board[i][j]);
                if(cnt%2==0 && Board[i][j]=='B')
                {
                    cnt++;
                    continue;
                }
                else if(cnt%2==0 && Board[i][j]=='W')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='B')
                {
                    cnt++;
                    sum++;
                    if(sum > * ResultSum) return;
                }
                else if(cnt%2!=0 && Board[i][j]=='W')
                {
                    cnt++;
                    continue;
                }
            }
        }
    }

    // printf("\nx : %d, y : %d, sum : %d\n", x, y, sum);
    * ResultSum = sum;
}

int main() {

    int i, j;
    int type=0; // 0:B, 1:W
    int X, Y; // 확인 위치
    int width,   // 8 <= width <= 50
         height;  // 8 <= height <= 50
    
    scanf("%d %d", &width, &height);
    int ResultSum = width*height; // 최대 width X height

    for(i=0; i<width; i++)
    {
        scanf("%s", &Board[i]);
    }

    for(X=0; X<=(width-8); X++)
    {
        for(Y=0; Y<=(height-8); Y++)
        {
            BCheckBoard(X, Y,&ResultSum);
            WCheckBoard(X, Y,&ResultSum);
        }
    }

    printf("%d", ResultSum);

  return 0;
}
```

숏코딩

```c
#include <stdio.h>
int n,m,ans = 100000;
char map[51][51];
int find(int p,int q)
{
	int white,black;
	white=black=0;
	for(int i=p;i<p+8;i++)
		for(int j=q;j<q+8;j++)
		{
			if((i+j)%2)
			{
				if(map[i][j]=='B') white++;
				else black++;
			}
			else
			{
				if(map[i][j]=='W') white++;
				else black++;
			}
		}

	if(white<black) return white;
	else return black;
}
int main()
{
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			scanf(" %1c",&map[i][j]);
	for(int i=0;i<=n-8;i++)
		for(int j=0;j<=m-8;j++)
		{
			int temp = find(i,j);
			if(ans>temp) ans = temp;
		}
	printf("%d",ans);
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char tmp;
	int N, M;
	int s, cnt;
	int min = 0x7fffffff;

	int arr[50][50] = {0,};

	scanf("%d %d", &N, &M);
	
	getchar();
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M+1; j++) {
			tmp = getchar();
			if (tmp != '\n') {
				arr[i][j] = tmp & 1;
			}
		}
	}

	for (int i = 0; i < N-7; i++) {
		for (int j = 0; j < M-7; j++) {
			for (s = 0; s < 2; s++) {
				
				cnt = 0;
				
				for (int k = 0; k < 8; k++) {
					for (int h = 0; h < 8; h++) {
						if (arr[i + k][j + h] != (i + k + j + h + s) % 2)
							cnt++;
					}
				}

				if (cnt < min)
					min = cnt;
			}
		}
	}

	printf("%d\n", min);
	
	return 0;
}
```

```c
#include <stdio.h>

int main() {

	int row, col;
	scanf("%d %d", &row,&col);
	char sample1[] = "WBWBWBWBWB";
	char sample2[] = "BWBWBWBWBW";
	char sample[2][8] = { "WBWBWBWB","BWBWBWBW" };

	// 입력
	char arr[50][50];
	for (int a = 0; a < row; a++) {
		scanf("%s", arr[a]);
	}

	int min = 64;
	int min_tmp = 0;

	for (int r = 0; r <= row - 8; r++) {		//시작 점의 행
		for (int c = 0; c <= col - 8; c++) {	//시작 점의 열
			
			for (int case_num = 0; case_num <= 1; case_num++) {
				min_tmp = 0;
				for (int a = 0; a < 8; a++) {
					for (int b = 0; b < 8; b++) {
						if (sample[(a + case_num) % 2][b] != arr[a + r][b + c]) 
							min_tmp++;
							
					}
				}
				if (min > min_tmp)
					min = min_tmp;
			}
	
		}
	}
	printf("%d", min);
}
```

```c
#include <stdio.h>
#include <stdlib.h>

char rightForm1[8][8] = {
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}
};

char rightForm2[8][8] = {
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
    {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}
};

void printBoard(char **board, int startR, int startC, int row, int col){
    int rowIdx, colIdx;
    
    for(rowIdx = startR; rowIdx < startR+row; rowIdx++){
        for(colIdx = startC; colIdx < startC+col; colIdx++){
            printf("%c", board[rowIdx][colIdx]);
        }
        printf("\n");
    }
}

int findRecolorNum(char **board, int startR, int startC){
    int answer;
    int row, col;
    int cor1 = 0, cor2 = 0;
    
    for(row = startR; row < startR + 8; row++){
        for(col = startC; col < startC + 8; col++){
            if(board[row][col] != rightForm1[row-startR][col-startC])
                cor1++;
            if(board[row][col] != rightForm2[row-startR][col-startC])
                cor2++;
        }
    }
    
    answer = (cor1 < cor2) ? cor1 : cor2;
    
    return answer;
}

int main(){
    int N, M;
    char **board;
    int row, col;
    char ch;
    int min = 64;
    int cur;
    
    scanf("%d %d", &N, &M);

    board = (char**)malloc(sizeof(char*) * N);

    for(row = 0; row < N; row++){
        board[row] = (char*)malloc(sizeof(char) * M);
        col = 0;
        while(col < M){
            ch = getc(stdin);

            if(ch != '\n' && ch != ' '){
                board[row][col] = ch;
                col++;
            }
        }
    }
    
    for(row = 0; row <= N-8; row++){
        for(col = 0; col <= M-8; col++){
            cur = findRecolorNum(board, row, col);
            min = cur < min ? cur : min;
        }
    }
    
    
    
    printf("%d", min);
    
    
    
    
    
    
    
}
```