import sys

sys.stdin = open('./1620.txt')

input_count, find_count = \
  map(int, sys.stdin.readline().split())

pokemon_name_dic = {}
pokemon_id_dic = []

# 사전 만들기
for i in range(1, input_count+1):

  # 키
  pokemon = sys.stdin.readline().rstrip()
  pokemon_id_dic.append(pokemon[0])

  # 키 만들기
  if (pokemon[0] not in pokemon_name_dic.keys()):
      pokemon_name_dic[pokemon[0]] = [[pokemon],[i]]
  else:
      pokemon_name_dic[pokemon[0]][0].append(pokemon)
      pokemon_name_dic[pokemon[0]][1].append(i)

# 비밀번호 찾기
for _ in range(find_count):
  key = sys.stdin.readline().rstrip()
  if (key.isdigit()):
    key = int(key)
    tmp_index = pokemon_name_dic[pokemon_id_dic[key-1]][1].index(key)
    print(pokemon_name_dic[pokemon_id_dic[key-1]][0][tmp_index])

  else:
    tmp_index = pokemon_name_dic[key[0]][0].index(key)
    print(pokemon_name_dic[key[0]][1][tmp_index])
