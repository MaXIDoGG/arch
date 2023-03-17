arr = [1, 2, 3, 4, 5]

print(arr[0:3])
print(arr[1:4]) #вывод срезов
print(arr[::-1]) #вывод списка в обратном порядке
print(";".join(list(map(str, arr)))) #вывод списка с разделителем ;

names = ['Дмитрий', 'Максим', 'Олег', 'Иван', 'Сергей']
print(list(zip(arr, names))) #результат операции zip

data = [i for i in range(0, 10) if i % 2 == 0] #генератор с условием
print(data)

data = [i + j for i in range(0, 5) for j in range(0, 5)] #генератор с вложенным циклом
print(data)

data = [(lambda i : i*i)(i) for i in range(0, 5)] #генератор с lambda-функцией
print(data)