from sys import stdin as input_data

input_data = open("./7576.txt")

def find_tomato(box):       # 입력은 문제에서 주어진 박스형식. 원소값이 1인 좌표의 리스트를 반환
    out =[]
    for i in range(len(box)):
        for j in range(len(box[i])):
            if(box[i][j] == 1):
                out.append((i,j))
    return out

temp = input_data.readline().split()
row = int(temp[1])
col = int(temp[0])

box = []

for i in range(row):
    temp = input_data.readline().split()
    for j in range(col):
        temp[j] = int(temp[j])
    box.append(temp)


day=0
stack1 = find_tomato(box)
stack2 = []

while(stack1!= [] or stack2!= []):
    if(stack1 != []):
        while(stack1 != []):
            i,j = stack1.pop()

            if(i-1 >=0 and box[i-1][j] == 0 ):      # 위쪽
                box[i-1][j] =1
                stack2.append((i-1,j))

            if(i+1<row and box[i+1][j] == 0):       #아래쪽
                box[i+1][j] = 1
                stack2.append((i+1,j))

            if( j+1<col and box[i][j+1]== 0 ):      #오른쪽
                box[i][j + 1] = 1
                stack2.append((i,j+1))
            if( j-1>=0 and box[i][j-1] == 0 ):      #왼쪽
                box[i][j-1] = 1
                stack2.append((i,j-1))
        day = day+1

    else:                                           #stack2가 안빈경우
        while(stack2 != []):
            i,j = stack2.pop()

            if (i - 1 >= 0 and box[i - 1][j] == 0 ):  # 위쪽
                box[i - 1][j] = 1
                stack1.append((i - 1, j))

            if (i + 1 < row and box[i + 1][j] == 0 ):  # 아래쪽
                box[i + 1][j] = 1
                stack1.append((i + 1, j))

            if (j + 1 < col and box[i][j + 1] == 0 ):  # 오른쪽
                box[i][j + 1] = 1
                stack1.append((i, j + 1))
            if (j - 1 >= 0 and box[i][j - 1] == 0 ):  # 왼쪽
                box[i][j - 1] = 1
                stack1.append((i, j - 1))
        day = day+1


for i in range(row):
    for j in range(col):
        if(box[i][j] == 0):
            day = -1
            break



#for x in box:
 #   print(x)
if(day ==-1):
    print(day)
else:
    print(day -1)
