 сортировка пузырьком
                                         2
 for i in range(n):                      n
     for j in range(n - 1):              n**2
         left = arr[j]                   2
         right = arr[j + 1]              2
         if left > right:                1
             arr[j] = right              2
             arr[j + 1] = left           2


O(n**2)


сортировка перемешиванием

left_index = 0                                           1
right_index = n - 1                                      1

while left_index <= right_index:                         n^2
                                                         2
    for i in range(left_index, right_index):             n
        left = arr[i]                                    2
        right = arr[i + 1]                               2
        if left < right                                  1
            arr[i] = right                               2
            arr[i + 1] = left                            2
    right_index = right_index - 1                        1
                                                         2
    for i in range(right_index, left_index, -1):         n
        right = arr[i]                                   2
        left = arr[i - 1]                                2
        if left < right:                                 1
            arr[i] = left                                2
            arr[i - 1] = right                           2
    left_index += 1                                      2

 O(n**2)



сортировка вставками

                                                        2
for i in range(n):                                      n
    val = arr[i]                                        2
    j = i - 1                                           1
    if j < 0:                                           1
        continue
    while val < arr[i] and j >= 0:                      n^2
        arr[j + 1] = arr[j]                             3
        j -= 1                                          1
    arr[j + 1] = val                                    2

 O(n**2)



сортировка выбором

                                                                        2
for i in range(n - 1):                                                  n - 1
    min_max_index = i                                                   1
    for j in range(i + 1, n):                                           n^2
        if arr[j] > arr[min_max_index]:                                 3
            min_max_index = j                                           1
            arr[i], arr[min_max_index] = arr[min_max_index], arr[j]     5

O(n**2)

сорторовка слиянием

     присутствуют 4 цикла for но не вложенных - n
     полно разных присвоений и сравнений      - какое то число )))
     разделение масива пополам потом опять и опять и слияние - log n    # вроде так

 result: O(n Log n)

быстрая сортировка

     циклы - n
     разделение масива пополам потом опять и опять и слияние - log n
     рекурсия - от 1 до n^2  в зависимости от опорного эл-та

 min O(n log n)
 max O(n**2)




