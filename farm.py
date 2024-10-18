import random
try:
    data = []
    for i in range(1,12):
        with open(f'input{str(i).zfill(2)}.txt','r',encoding="utf-8" ) as input_file:
            lines=input_file.readlines()
            for item in lines:
                data.append(item)
    print(data)
except FileNotFoundError:
    print("Файл не найден.")