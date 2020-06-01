class Matrix:
    def __init__(self, x):
        self.x = x
        #self.y = y

    def __add__(self, other):
        #a=[]
        #for i in range(len(self.x)):
        #    b =
        return Matrix([[self.x[i][j] +other.x[i][j] for j in range(len(self.x[i]))] for i in range(len(self.x))])

    # def __str__(self):
    #     return str(self.x)
    def __str__(self):
        # for i in range(len(self.x)):
        #return "_".join(str([self.x[i] for i in range(len(self.x)) ]))
        #return " ".join(str(self.x))
        a = [str(self.x[i]) for i in range(len(self.x))]
        #return "_".join(a)
        return "\n".join(a)


mmatrix_1 = Matrix([[10,10],
                    [10,10],
                    [10,10]])
mmatrix_2 = Matrix([[15,20],
                    [30,40],
                    [50,60]])
print(mmatrix_1 + mmatrix_2)

