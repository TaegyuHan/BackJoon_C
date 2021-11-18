from sys import stdin as input

# input = open("./1041.txt")

N = int(input.readline())
facet = list(map(int, input.readline().split()))
facet_number = [ min(facet[0], facet[5]), # A F
                 min(facet[1], facet[4]), # B E
                 min(facet[2], facet[3]) ] # C D
facet_number.sort()

if N == 1:
    print(sum(facet) - max(facet))
    exit()

result = 0

# 1면
tmp_multip = ((N - 1)*(N - 2)*4 + (N - 2)*(N - 2))
result += facet_number[0]*tmp_multip

# 2면
tmp_multip = (2*N - 3)*4
result += sum(facet_number[0:2])*tmp_multip

# 3면
result += sum(facet_number)*4

print(result)