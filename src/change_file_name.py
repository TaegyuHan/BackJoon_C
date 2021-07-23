
# 폴더안의 파일 이름변경 코드

import os

path = "C:\github\BackJoon_C\\as"
folder_list = os.listdir(path)

for folder in folder_list:
    os.chdir(path + '\\' + folder)
    file_name = os.listdir(os.getcwd())[0]
    print("변경완료 %s > %s", file_name, "README.md")
    os.rename(file_name, "README.md")