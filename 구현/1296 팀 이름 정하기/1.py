import sys
from typing import List


class TeamNameFinder:

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._team_name: str = ""
        self._name_point: int = 0

    def set_team_name(self, team_name: str) -> None:

        # 이름에서 L 개수 확인
        L: int = self._check_count_alphabet(alpha='L', team_name=team_name)
        O: int = self._check_count_alphabet(alpha='O', team_name=team_name)
        V: int = self._check_count_alphabet(alpha='V', team_name=team_name)
        E: int = self._check_count_alphabet(alpha='E', team_name=team_name)
        point: int = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

        if self._name_point <= point:

            if self._team_name == "":  # 팀 이름 첫 등록인 경우
                self._team_name = team_name
                self._name_point = point

            if team_name < self._team_name:
                self._team_name = team_name
                self._name_point = point

    def _check_count_alphabet(self, alpha: str, team_name: str) -> int:
        count = 0
        for tmp_alpha in self._name:
            if tmp_alpha == alpha:
                count += 1

        for tmp_alpha in team_name:
            if tmp_alpha == alpha:
                count += 1

        return count

    def answer(self) -> str:
        return self._team_name


if __name__ == "__main__":

    # with open("6.txt", "r") as f:
    #     name: str = f.readline()
    #     team_input_count: int = int(f.readline())
    #     team_names: List[str] = [f.readline().strip() for _ in range(team_input_count)]

    name: str = sys.stdin.readline()
    team_input_count: int = int(sys.stdin.readline())
    team_names: List[str] = [sys.stdin.readline().strip() for _ in range(team_input_count)]

    finder: TeamNameFinder = TeamNameFinder(name)
    for team_name in team_names:
        finder.set_team_name(team_name)

    print(finder.answer(), end="")
