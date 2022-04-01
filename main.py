import tkinter as tk
import random
from copy import deepcopy


# Primov Orozbek
# 1 class, 5 methods, 2 private variables, 1 private method

class Life:
    def __init__(self, n, m, width, height, c):
        self.matrix = []
        self.width = width
        self.height = height
        self.n = n
        self.m = m
        self.c = c

        for i in range(n):
            row = []
            for j in range(m):
                row.append(random.choice((0, 1)))
                # row.append(0)
            self.matrix.append(row)

        # self.matrix[2][0] = 1
        # self.matrix[3][1] = 1
        # self.matrix[3][2] = 1
        # self.matrix[2][2] = 1
        # self.matrix[1][2] = 1

    def display(self):
        for i in self.matrix:
            print(' '.join(map(str, i)))
        print()

    def count_adj(self, i, j, matrix_clone):
        nn = 0
        i_up, i_do, j_le, j_ra = i - 1, i + 1, j - 1, j + 1
        if i == 0:
            i_up = self.n - 1
        if i == self.n - 1:
            i_do = 0
        if j == 0:
            j_le = self.m - 1
        if j == self.m - 1:
            j_ra = 0

        nn += matrix_clone[i_up][j]
        nn += matrix_clone[i_up][j_ra]
        nn += matrix_clone[i][j_ra]
        nn += matrix_clone[i_do][j_ra]
        nn += matrix_clone[i_do][j]
        nn += matrix_clone[i_do][j_le]
        nn += matrix_clone[i][j_le]
        nn += matrix_clone[i_up][j_le]
        return nn

    def __step(self):
        matrix_clone = deepcopy(self.matrix)

        for i in range(self.n):
            for j in range(self.m):
                nn = self.count_adj(i, j, matrix_clone)

                if nn not in (2, 3):
                    self.matrix[i][j] = 0
                elif nn == 3:
                    self.matrix[i][j] = 1
                # print(nn, i, j)

    def draw(self):
        self.c.delete('all')
        size_width = self.width / self.m
        size_height = self.height / self.n
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j]:
                    color = "green"
                else:
                    color = "white"
                self.c.create_rectangle(j * size_width, i * size_height, (j+1) * size_width, (i+1) * size_height, fill=color, outline='')
        self.__step()
        self.c.after(100, self.draw)

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        if n not in range(5, 101):
            raise Exception('The number of rows should be in the range of 5-100')
        self.__n = n  # Private variable

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, m):
        if m not in range(5, 101):
            raise Exception('The number of columns should be in the range of 5-100')
        self.__m = m  # Private variable


root = tk.Tk()
root.geometry('720x720')

canvas = tk.Canvas(root, width=720, height=720)
canvas.pack()

number_of_rows = int(input('Enter number of rows: '))
number_of_cols = int(input('Enter number of columns: '))

game = Life(number_of_rows, number_of_cols, 720, 720, canvas)


game.display()
game.draw()

root.mainloop()
