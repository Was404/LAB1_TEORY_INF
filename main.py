# This is a sample Python script.
import numpy as np
import math
def create_matrx():
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
    
    if m[0,0] == 1 and m[1, 1] == 1 and m[2, 2] == 1 and m[1,0] == 0 and m[2,0] == 0 and m[0,1] == 0 and m[0,2] == 0 and m[1,2] == 0 and m[2, 1] == 0:
        p = np.array([[m[0,3], m[0,4], m[0,5], m[0,6]], [m[1,3], m[1,4], m[0,5], m[0,6]], [m[2,3], m[2,4], m[0,5], m[2,6]]], dtype=int)
        ig = np.array([[m[0,0], m[0,1],m[0,2]], [m[1,0], m[1,1], m[1,2]], [m[2,0], m[2,1], m[2,2]]])
    elif m[0,0] == 0 or m[0,1] == 1 or m[0,2] == 1:
            for i in range(m):
                 if m[0,i] == 1 and m[1,i] == 0 and m[2,i] == 0:
                      nos = m[0,0]
                      m[0,0] = m[0,i]
                      m[0,i] = nos #здесь замена
                      m[1,i] = m[1,0]
                      m[2,i] = m[2,0]
            p = np.array([[m[0,3], m[0,4], m[0,5], m[0,6]], [m[1,3], m[1,4], m[0,5], m[0,6]], [m[2,3], m[2,4], m[0,5], m[2,6]]], dtype=int)
            ig = np.array([[m[0,0], m[0,1],m[0,2]], [m[1,0], m[1,1], m[1,2]], [m[2,0], m[2,1], m[2,2]]])
    elif m[1,1] == 0 or m[0,1] == 1 or m[2,1] == 1:
            for i in range(m):
                 if m[1,i] == 1 and m[0,i] == 0 and m[2,i] == 0:
                      nos = m[1,1]
                      m[1,1] = m[1,i]
                      m[1,i] = nos #здесь замена
                      m[0,i] = m[0,1]
                      m[2,i] = m[2,1]
            p = np.array([[m[0,3], m[0,4], m[0,5], m[0,6]], [m[1,3], m[1,4], m[0,5], m[0,6]], [m[2,3], m[2,4], m[0,5], m[2,6]]], dtype=int)
            ig = np.array([[m[0,0], m[0,1],m[0,2]], [m[1,0], m[1,1], m[1,2]], [m[2,0], m[2,1], m[2,2]]])          
    elif m[2,2] == 0 or m[2,0] == 1 or m[2,1] == 1:
            for i in range(m):
                 if m[2,i] == 1 and m[0,i] == 0 and m[1,i] == 0:
                      nos = m[2,2]
                      m[2,2] = m[2,i]
                      m[2,i] = nos #здесь замена
                      m[0,i] = m[0,2]
                      m[1,i] = m[1,2]
            p = np.array([[m[0,3], m[0,4], m[0,5], m[0,6]], [m[1,3], m[1,4], m[0,5], m[0,6]], [m[2,3], m[2,4], m[0,5], m[2,6]]], dtype=int)
            ig = np.array([[m[0,0], m[0,1],m[0,2]], [m[1,0], m[1,1], m[1,2]], [m[2,0], m[2,1], m[2,2]]])                                          
    p_trancp = p.transpose()
    nk = culmns - rows
    I = np.eye(nk, nk, dtype=int)  #это создание единичн матрицы
    
    g_sys = np.hstack((ig, p))
    print("g_sys:\n", g_sys)
    h_sys = np.hstack((p_trancp, I))
    print("Систематический вид:\n", h_sys)

    # inf words массив из (n,k)
    inf_words = np.array([[0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]])
    #inf_words_vector = np.array([0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1 , 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1])
    print("Информационные слова:\n", inf_words)

    cod_word_c = g_sys.dot(inf_words)
    prod_vector = np.dot(inf_words, g_sys)
    for j in range(len(prod_vector)):
        if (prod_vector[j] % 2 == 0):
            prod_vector[j] = 0
        else:
            prod_vector[j] = 1
    
    cod_word_c = prod_vector
    print("Кодовые слова:\n", cod_word_c) 
    
    code_words_or_syndromes = []
    code_words_or_syndromes.append(cod_word_c)
    wtn = np.count_nonzero(cod_word_c)     #РАБОТАЕТ НЕ ТРОЖЪ 
    print("WTN:\n", wtn)
    return wtn    
    #except Exception:
    #        print("Error")
    

# получаем d минимальное
def get_d_min(wtn):
    # делаем копию, чтобы не менять исходную
    wtn = list(wtn)
    while 0 in wtn:
        wtn.remove(0)
    d_min = min(wtn)
    return d_min
    
def matrix_check():
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
    
    cod_word = 2**rows
    nk = culmns - rows
    if m[0,4] == 1 and m[1, 5] == 1 and m[2, 6] == 1:
        I =  np.eye(nk, nk, dtype=int) 
        p = np.array([[m[0,0], m[0,1], m[0,2], m[0,3]], [m[1,0], m[1,1], m[1,2], m[1,3]], [m[2,0], m[2,1], m[3,2], m[4,3]]], dtype=int)
    H_sys = np.hstack((p, I))
    p_trance = p.transpose()
    print("Hsys:\n", H_sys)
    print("P transpone:\n", p_trance)    

def help():
     print("Python scrypt for matrix. How to use:\nCommands:\n", "-help"," "," "," "," "," ","Documentation\n")







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('######################################\nMatrix representation of block codes\n######################################\n')
    print("Перед началом введите матрицу в файл m.txt или\nдобавьте свой txt файл в корень проекта с именем m\n--------------------------------")

    print("Какая матрица поступает на вход?\n(1)Пораждающая\n(2)Проверочная\n(Для справочной информации введите -help)")
    question = input()
    if question == "Пораждающая" or question == "1":
        create_matrx()
    elif question == "Проверочная" or question == "2":
        print("Я не готов к этому")
        matrix_check()
    elif question == "-help":
         help()
    else:
        print("Вы не выбрали тип матрицы")    
    # write_matrix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
