from sys import stdin as input

class P2468:
    def input_data(self):
        self.N = int(input.readline())
        self.answer = 0
        self.max_height = 0
        self.ground = []
        for _ in range(self.N):
            tmp = list(map(int, input.readline().split()))
            self.max_height = max(tmp + [self.max_height])
            self.ground.append(tmp)

    def _BFS(self, i, j, max_height):
        # 상 우 하 좌
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        visited = [(i, j)]
        while visited:
            ni, nj = visited.pop()
            self.visited[ni][nj] = True
            for idx in range(4):
                nx = ni + dx[idx]
                ny = nj + dy[idx]

                if nx < 0 or nx >= self.N: continue
                if ny < 0 or ny >= self.N: continue
                if self.visited[nx][ny]: continue
                if self.ground[nx][ny] < max_height: continue

                visited.append((nx, ny))

    def result(self):
        for height in range(self.max_height):
            self.visited = [[False]*self.N for _ in range(self.N)]
            safe_ground = 0
            for i in range(self.N):
                for j in range(self.N):
                    if self.ground[i][j] > height and not self.visited[i][j]:
                        safe_ground += 1
                        self.visited[i][j] = True
                        self._BFS(i, j, height)
            self.answer = max(self.answer, safe_ground)
            print(self.answer)



if __name__ == '__main__':
    input = open("./2468.txt")
    P = P2468()
    P.input_data()
    P.result()