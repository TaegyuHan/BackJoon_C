import unittest
from main import P

class TestSum(unittest.TestCase):

    OUTPUT_DIR_PATH = "./data/output/"

    def _answer_data(self, file_name: str):
        """ 데이터 받기 """
        result_data = []
        with open(file_name, encoding="utf-8") as input:
            while tmp := input.readline():
                result_data.append(int(tmp))
        return result_data

    def test_1(self):
        file_name = "1.txt"
        p = P(file_name=file_name)
        result_data = p.answer_test()
        answer_data = self._answer_data(file_name=f"{self.OUTPUT_DIR_PATH}{file_name}")
        self.assertListEqual(answer_data, result_data)

    def test_2(self):
        file_name = "2.txt"
        p = P(file_name=file_name)
        result_data = p.answer_test()
        answer_data = self._answer_data(file_name=f"{self.OUTPUT_DIR_PATH}{file_name}")
        self.assertEqual(answer_data, result_data)

    def test_3(self):
        file_name = "3.txt"
        p = P(file_name=file_name)
        result_data = p.answer_test()
        answer_data = self._answer_data(file_name=f"{self.OUTPUT_DIR_PATH}{file_name}")
        self.assertListEqual(answer_data, result_data)

    def test_4(self):
        file_name = "4.txt"
        p = P(file_name=file_name)
        result_data = p.answer_test()
        answer_data = self._answer_data(file_name=f"{self.OUTPUT_DIR_PATH}{file_name}")
        self.assertEqual(answer_data, result_data)


if __name__ == '__main__':
    unittest.main()