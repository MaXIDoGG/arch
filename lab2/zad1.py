import numpy

A = [[float(input()) for j in range(3)] for i in range(3)]
b = [float(input()) for j in range(3)]

x = numpy.linalg.solve(A, b)  # Решение СЛАУ

s = 'Решение: '
for i in range(len(x)):
    s += str(x[i])
    if i != len(x) - 1:
        s += ', '
print(s)

check = 0
for i in range(3):
    if A[i][0]*x[0] + A[i][1]*x[1] + A[i][2]*x[2] != b[i]:
        check = 1
        break

if check == 0:
    print("Решение оказалось точным")
else:
    discr = []
    for i in range(3):
        discr.append(b[i] - (A[i][0]*x[0] + A[i][1]*x[1] + A[i][2]*x[2]))

    s = 'Невязки: '
    for i in range(len(discr)):
        s += str(discr[i])
        if i != len(discr) - 1:
            s += ', '
    print(s)
