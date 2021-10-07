from sys import stdin as input_data

input_data = open("./1697.txt")
me, brother = map(int, input_data.readline().split())
current_location = (me, brother - me)
result_count = 0

def next_time(location, brother):
    me = location[0]
    teleporting = (me*2, abs(brother - (me*2)))
    next = (me + 1, abs(brother - (me + 1)))
    back = (me - 1, abs(brother - (me - 1)))

    return (teleporting, next, back)


while True:
    result_count += 1
    tmp_distance = abs(brother - me)
    for i, next_location in enumerate(next_time(current_location, brother)):
          me = next_location[0]
          teleporting = (me*2)
          next = (me + 1)
          back = (me - 1)
          for me in (teleporting, next, back):
              if (tmp := abs(brother - me)) < tmp_distance:
                  current_location = (me, tmp)
                  tmp_distance = tmp

    if tmp_distance == 0:
        print(result_count)
        break
