"""Solution code for "BaekJoon 에디터".

- Problem link: https://www.acmicpc.net/problem/1406
"""

from sys import stdin as input


class Node:

    def __init__(self, data: str) -> None:
        self.front: Node = None
        self.back: Node = None
        self.data: str = data


class Cursur:

    def __init__(self) -> None:
        self.front: Node = None
        self.back: Node = None


class LinkedList:
    """ 링크드 리스트 생성 """

    def __init__(self):
        # 링크드 리스트 생성
        self.link = Node("start")
        end_node = Node("end")
        self.link.back = end_node
        end_node.front = self.link

        # 커서 생성
        self.cursur = Cursur()
        self.cursur.front = self.link
        self.cursur.back = self.link.back

    def front(self):
        """ 링크드 리스트의 첫번째 노드 """
        return self.link

    def back(self):
        """ 링크드 리스트의 마지막 노드 """
        tmp = self.link
        while tmp.data != "end":
            tmp = tmp.back
        return tmp

    def show(self):
        """ 링크드 리스트의 데이터 확인 """
        tmp = self.link.back
        while tmp.data != "end":
            print(tmp.data, end="")
            tmp = tmp.back

    def insert(self, data):
        """ 커서 왼쪽에 추가함 """
        node = Node(data)

        # 커서 앞부분 노드와 연동
        self.cursur.front.back = node
        node.front = self.cursur.front
        self.cursur.front = node

        # 커서 뒷부분 노드와 연동
        self.cursur.back.front = node
        node.back = self.cursur.back

    def remove(self):
        """ 커서 왼쪽에 있는 문자를 삭제함 """
        if self.cursur.front.data == "start":
            return

        # 링크드 리스트 연결
        self.cursur.front.front.back = self.cursur.back
        self.cursur.back.front = self.cursur.front.front

        self.cursur.front = self.cursur.front.front

    def cursur_front(self):
        """ 커서 앞으로 이동 """
        # 맨 앞이면 이동 안함
        if self.cursur.front.data == "start":
            return

        # 앞으로 이동
        self.cursur.back = self.cursur.front
        self.cursur.front = self.cursur.front.front

    def cursur_back(self):
        """ 커서 뒤로 이동 """
        # 맨 뒤면 이동 안함
        if self.cursur.back.data == "end":
            return

        # 앞으로 이동
        self.cursur.front = self.cursur.back
        self.cursur.back = self.cursur.back.back


class P:

    def __init__(self) -> None:
        # 문자열 입력
        self.string: list[str] = list(input.readline().strip())

        # 명령어 숫자
        self.command_count = int(input.readline())
        self.linked_list = LinkedList()

    def _make_linked_list(self):
        """ 기존 문자열 데이터 넣기 """
        for data in self.string:
            self.linked_list.insert(data)

    def _input_command(self):
        """ 명령어 입력받기 """
        for _ in range(self.command_count):
            command = input.readline().strip()
            if command[0] == "L":
                self.linked_list.cursur_front()
            elif command[0] == "D":
                self.linked_list.cursur_back()
            elif command[0] == "P":
                data = command.split()
                self.linked_list.insert(data[-1])
            elif command[0] == "B":
                self.linked_list.remove()

    def result(self) -> None:
        self._make_linked_list()
        self._input_command()
        self.linked_list.show()


if __name__ == '__main__':
    # input = open('./1406.txt')
    P = P()
    P.result()