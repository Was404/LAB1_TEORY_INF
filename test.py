import numpy as np

def hamming_encode(arr):
    # Определяем количество дополнительных битов для массива
    for i in range(len(arr)):
        if 2 ** i >= len(arr) + i + 1:
            m = i
            break
    
    # Добавляем дополнительные биты
    encoded_arr = np.zeros(len(arr) + m, dtype=int)
    j = 0
    for i in range(len(encoded_arr)):
        if i+1 != 2**j:
            encoded_arr[i] = arr[j]
            j += 1
    
    # Размещаем биты в матрице кода Хэмминга
    matrix = np.zeros((m, len(encoded_arr)), dtype=int)
    for i in range(m):
        # Для каждой строки вычисляем значение битов
        row_bits = []
        for j in range(1, len(encoded_arr)+1):
            if (j // 2**(i)) % 2 == 1:
                row_bits.append(encoded_arr[j-1])
        # Вычисляем значение проверочного бита
        matrix[i][2**i-1] = sum(row_bits) % 2
        # Заполняем матрицу
        for j in range(len(encoded_arr)):
            if (j+1) not in [2**i-1 for i in range(m)]:
                matrix[i][j] = encoded_arr[j]
    
    # Заменяем значения проверочных битов на четные/нечетные значения
    for i in range(m):
        row_bits = matrix[i, :]
        num_ones = sum(row_bits)
        if num_ones % 2 == 0:
            matrix[i][2**i-1] = 1
        else:
            matrix[i][2**i-1] = 0
    
    # Возвращаем закодированный массив
    return matrix[:, :-m].flatten()

if __name__ == '__main__':
    f = open('m.txt', 'r')
    matrix = [line.replace("\n", "").split() for line in f]

    arr = np.array(matrix, dtype = int)
    print("Получена матрица:\n", arr)

    encoded_arr = hamming_encode(arr)
    print(encoded_arr)
