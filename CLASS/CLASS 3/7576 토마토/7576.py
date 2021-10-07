from sys import stdin as input_data

# input_data = open("./7576.txt")

width, height = \
    map(int, input_data.readline().split())

ripe_tomatoes_position = []

tomatoes_state = { 'ripe_tomato_cnt': 0,
                   'empty_tomato_cnt': 0 }

box = []

def check_tomato(x, y) -> bool:
    if box[x][y] == 0:
        box[x][y] = 1
        return True
    else:
        return False

def check_indexing(location) -> bool:
    x, y = location
    if (0 <= x and x < len(box)) and  \
        (0 <= y and y < len(box[0])):
        return True
    else:
        return False


def next_tomato(location) -> None:
    x, y = location

    left = x, y - 1
    right = x, y + 1
    up = x + 1, y 
    down = x - 1, y 

    for direction in [left, right, up, down]:
        if check_indexing(direction):
                if check_tomato(direction[0], direction[1]):
                    tmp_tomatoes_position.append((direction[0], direction[1]))


for i in range(height):
    tmp_box = []
    for j, num in enumerate(map(int, input_data.readline().split())):
        tmp_box.append(num)
        if num == 0:
            pass
        elif num == 1:
            ripe_tomatoes_position.append((i, j))
        else:
            tomatoes_state['empty_tomato_cnt'] += 1
    box.append(tmp_box)

result = -1
while ripe_tomatoes_position:

    tomatoes_state['ripe_tomato_cnt'] += len(ripe_tomatoes_position)

    tmp_tomatoes_position = []
    result += 1
    for x, y in ripe_tomatoes_position:
        next_tomato((x, y))

    ripe_tomatoes_position = tmp_tomatoes_position.copy()


if (tomatoes_state['ripe_tomato_cnt'] 
    + tomatoes_state['empty_tomato_cnt']) == width*height:
    print(result)
else:
    print(-1)