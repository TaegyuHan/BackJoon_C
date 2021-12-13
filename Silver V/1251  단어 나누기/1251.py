from sys import stdin as input

class P1251:

    def input_data(self):
        self.sting = input.readline()
        self.sting_len = len(self.sting)

    def result(self):
        self.answer = []
        for i in range(1, self.sting_len - 1):
            for j in range(i + 1, self.sting_len):
                    tmp_string = (
                        f"{self.sting[:i][::-1]}"
                        f"{self.sting[i:j][::-1]}"
                        f"{self.sting[j:][::-1]}"
                    )
                    self.answer.append(tmp_string)

        print(min(self.answer))

if __name__ == '__main__':
    input = open("./1251.txt")
    P = P1251()
    P.input_data()
    P.result()
