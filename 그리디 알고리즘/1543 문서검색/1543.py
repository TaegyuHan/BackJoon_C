from sys import stdin as input

# input = open("./1543.txt")

string = input.readline().rstrip()
sl = len(string)

search_string = input.readline().rstrip()
ssl = len(search_string)

index = 0
result = 0
while True:
    if search_string == string[index:(index + ssl)]:
        result += 1
        index += ssl
    else:
        index += 1

    if index > sl:
        break

print(result)


