from sys import stdin as input

# input = open("./1041.txt")

N = int(input.readline())
facet = list(map(int, input.readline().split()))
facet_number = [ min(facet[0], facet[5]),
                 min(facet[1], facet[4]),
                 min(facet[2], facet[3]) ]
facet_number.sort()

if N == 1:
    print(sum(facet) - max(facet))
    exit()

result = 0
tmp_multip = ((N - 1)*(N - 2)*4 + (N - 2)*(N - 2)) # 1면
result += facet_number[0]*tmp_multip

tmp_multip = (2*N - 3)*4 # 2면
result += sum(facet_number[0:2])*tmp_multip
result += sum(facet_number)*4 # 3면

print(result)