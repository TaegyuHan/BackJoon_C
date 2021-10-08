from sys import stdin as input_data

input_data = open("./1697.txt")
me, brother = map(int, input_data.readline().split())

def next_time(me):
    return (me*2, me + 1, me -1 )

result = 0
while True:
    
    if me == brother:
        break
    
    result += 1
    
    tmp_distance = abs(me - brother)
    for next in next_time(me):
        for next_me in (next*2, next + 1, next - 1):
            if (tmp := abs(next_me - brother)) < tmp_distance:
                tmp_distance = tmp
                me = next
                
    if tmp_distance
        

print(result)
