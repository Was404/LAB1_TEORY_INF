# This is a sample Python script.
import numpy as np

def create_matrx():
    global matrix
    #try:
    f = open('m.txt', 'r')
    matrix = [line.replace("\n", "").split() for line in f]
    #print(matrix) #Это по строкам матрица
    m = np.array(matrix, dtype = int)
    print("Получена матрица:\n", m)
    rows, culmns = m.shape
    speed = rows/culmns
    q = 2**rows
    print("---------------------------------\nk:", rows, "\nn:", culmns, "\nCкорость кода:", speed,"\nМощность алфавита:", q ,"\n---------------------------------\n")
    
    if m[0,0] == 1 and m[1, 1] == 1 and m[2, 2] == 1:
        print(m.dtype)
        p = np.array([[m[0,3], m[0,4], m[0,5], m[0,6]], [m[1,3], m[1,4], m[0,5], m[0,6]], [m[2,3], m[2,4], m[0,5], m[2,6]]], dtype=int)
        
    p_trancp = p.transpose()
    nk = culmns - rows
    I = np.eye(nk, nk, dtype=int)  #это создание единичн матрицы
    h_sys = np.hstack((p_trancp, I))
            #print("Транспонированная матрица:\n\n", m_trancp)
    #inf_words = np.arange(0, 1)
    print("Систематический вид:\n", h_sys)

    inf_words = np.indetity((rows, culmns))
    print(inf_words)
    #except Exception:
    #        print("Error")
    #return matrix


def matrix_check(matrix):
    with open('output.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')
    f = open('m.txt', 'r')
    matrix = [line.replace("\n", "").split() for line in f]
    #print(matrix) #Это по строкам матрица
    m = np.array(matrix, dtype = int)
    print("Получена матрица:\n", m)
    rows, culmns = m.shape
    speed = rows/culmns
    q = 2**rows
    print("---------------------------------\nk:", 
          rows, "\nn:", culmns, "\nCкорость кода:", speed,"\nМощность алфавита:", q ,
          "\n---------------------------------\n")
      

def help():
     print("Python scrypt for matrix. How to use:\nCommands:\n", "-help"," "," "," "," "," ","Documentation\n")







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(
        '######################################\nMatrix representation of block codes\n######################################\n')
    print("Перед началом введите матрицу в файл m.txt или\nдобавьте свой файл в корень проекта с именем m\n-------------------------")

    print("Какая матрица поступает на вход?\n(1)Пораждающая\n(2)Проверочная\n(Для справочной информации введите -help)")
    question = input()
    if question == "Пораждающая" or question == "1":
        matrix_check()
    elif question == "Проверочная" or question == "2":
        print("Я не готов к этому")
    elif question == "-help":
         help()
    else:
        print("Вы не выбрали тип матрицы")    
    # write_matrix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
