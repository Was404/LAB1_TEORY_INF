# This is a sample Python script.
import numpy as np

def create_matrx():
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    global matrix
    print("Какая матрица поступает на вход?\n(1)Пораждающая\n(2)Проверочная")
    question = input()
    if question == "Пораждающая" or question == "1":
        try:
            f = open('m.txt', 'r')
            matrix = [line.replace("\n", "").split() for line in f]
            #print(matrix) #Это по строкам матрица
            m = np.array(matrix)
            print("Получена матрица:", m)
            rows, culmns = m.shape
            speed = rows/culmns
            q = 2**rows
            print("---------------------------------\nk:", rows, "\nn:", culmns, "\nCкорость кода:", speed,"\nМощность алфавита:", q ,"\n---------------------------------\n")
            Gsys = np.eye(3, 3, dtype=int) #это создание единичн матрицы
            print("Gsys:", Gsys)
            m_trancp = m.transpose()
        except:
            print("Error")
    elif question == "Проверочная" or question == "2":
        print("Я не готов к этому")
    else:
        print("Вы не выбрали тип матрицы")
    return matrix


def write_matrix(matrix):
    with open('output.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(
        '######################################\nMatrix representation of block codes\n######################################\n')
    create_matrx()
    # write_matrix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
