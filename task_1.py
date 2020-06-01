import numpy as np


class Matrix(object):
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        a,b=[],[]

        for i in range(len(self.x)):
            for j in range(len(self.x[i])):
                a.append((self.x[i][j] + other.x[i][j]))
            b.append(a)
            a=[]
        return b

    def __str__(self):
        a = [str(self.x[i]) for i in range(len(self.x))]
        return "\n".join(a)


matrix_1 = [[12,13,14], [15,16,17]]
matrix_2 = [[10,20,30], [40,50,60]]
matrix_3= Matrix(matrix_1)+Matrix(matrix_2)

print(f"{Matrix(matrix_1)}\n+\n{Matrix(matrix_2)}\n=\n{Matrix(matrix_3)}")

if (np.array(matrix_1) + np.array(matrix_2)).tolist() == matrix_3:
    print("\nМатрицы равны, задание выполненно верно")
