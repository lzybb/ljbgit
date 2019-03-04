import tkinter
import random

class Food():

    def __init__(self, Snk_list):
        self.Snk_list = Snk_list

        s1 = set(self.Snk_list)
        s = canvas_set.difference(s1)

        self.Food_list = list(s)
        self.Food_point = random.choice(self.Food_list)

        self.make_point()

    def make_point(self):
        return self.Food_point


class Snk():

    def __init__(self, Snk_list, Food_point, move_x=0, move_y=0):

        self.Snk_list = Snk_list
        self.Food_point = Food_point
        self.move_x = move_x
        self.move_y = move_y

        l = len(self.Snk_list)
        self.move_pointx = self.Snk_list[l - 1][0] + (self.move_x * px)
        self.move_pointy = self.Snk_list[l - 1][1] + (self.move_y * px)
        self.move_point = (self.move_pointx, self.move_pointy)


    def Snk_isover(self):

        if self.move_pointx < 0 or self.move_pointx >= canvas_w:
            return True
        elif self.move_pointy < 0 or self.move_pointy >= canvas_h:
            return True
        elif self.move_point in self.Snk_list:
            if self.move_x != 0 or self.move_y != 0:
                return True
            else:
                return False
        else:
            return False

    def Snk_move(self):

        if self.move_point == self.Food_point:
            self.Snk_list.append(self.move_point)
            i = Food(self.Snk_list)
            self.Food_point = i.make_point()
            return self.Food_point, self.Snk_list

        else:
            if self.move_x !=0 or self.move_y !=0:
                self.Snk_list.remove(self.Snk_list[0])
                self.Snk_list.append(self.move_point)
                return self.Food_point, self.Snk_list
            else:
                return self.Food_point, self.Snk_list


class Win(tkinter.Tk):

    def __init__(self, a=500, b=600, c=10):
        global px
        px = int(c)
        w = int(a)
        h = int(b)
        w = w // px
        h = h // px
        global canvas_w
        canvas_w = w * px
        global canvas_h
        canvas_h = h * px

        # 像素点的集合
        canvas_list = list()
        for i in range(1, w):
            for j in range(1, h):
                canvas_list.append((i * px, j * px))
        global canvas_set
        canvas_set = set(canvas_list)

        # 创建画板
        tkinter.Tk.__init__(self)
        self.canvas = tkinter.Canvas(self, width=canvas_w, height=canvas_h, bg='gray')
        self.canvas.grid(row=2)

        # 创建初始Snk
        self.Snk_list = list()
        # 点1
        x1 = (w // 2) * px
        y1 = (h // 2) * px
        p1 = (x1, y1)
        # 点2
        x2 = (w // 2) * px + px
        y2 = (h // 2) * px
        p2 = (x2, y2)
        # 点3
        x3 = (w // 2) * px + px * 2
        y3 = (h // 2) * px
        p3 = (x3, y3)
        self.Snk_list.append(p1)
        self.Snk_list.append(p2)
        self.Snk_list.append(p3)
        self.Snk = self.canvas.create_line(self.Snk_list, fill='green', width=px)

        # 创建初始Food
        i = Food(self.Snk_list)
        self.Food_point = i.make_point()
        self.Food = self.canvas.create_rectangle(self.Food_point[0]-px//2, self.Food_point[1]-px//2,
                                                 self.Food_point[0]+px//2, self.Food_point[1]+px//2,
                                                 fill='red', outline='green')

        # 初始跑动
        self.run()
        self.automatic_run()

    def run(self, move_x=0, move_y=0):

        i = Snk(self.Snk_list, self.Food_point, move_x, move_y)
        isover = i.Snk_isover()
        self.Food_point, self.Snk_list = i.Snk_move()
        # 进行判断
        if isover == False:
            self.canvas.delete(self.Snk)

            self.Snk = self.canvas.create_line(self.Snk_list, fill='green', width=px)

            self.canvas.delete(self.Food)
            self.Food = self.canvas.create_rectangle(self.Food_point[0]- px//2, self.Food_point[1]-px//2,
                                                     self.Food_point[0] + px//2, self.Food_point[1] + px//2,
                                                     fill = 'red', outline = 'green')
        else:
            self.game_over()



    def move_up(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][1] == self.Snk_list[ls - 2][1]:
            self.run(0, -1)
        else:
            if self.Snk_list[ls - 1][1] < self.Snk_list[ls - 2][1]:
                self.run(0, -1)
            else:
                self.run(0, 0)

    def move_down(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][1] == self.Snk_list[ls - 2][1]:
            self.run(0, 1)
        else:
            if self.Snk_list[ls - 1][1] > self.Snk_list[ls - 2][1]:
                self.run(0, 1)
            else:
                self.run(0, 0)

    def move_left(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][0] == self.Snk_list[ls - 2][0]:
            self.run(-1, 0)
        else:
            if self.Snk_list[ls - 1][0] < self.Snk_list[ls - 2][0]:
                self.run(-1, 0)
            else:
                self.run(0, 0)

    def move_right(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][0] == self.Snk_list[ls - 2][0]:
            self.run(1, 0)
        else:
            if self.Snk_list[ls - 1][0] > self.Snk_list[ls - 2][0]:
                self.run(1, 0)
            else:
                self.run(0, 0)

    def automatic_run(self):
        ls = len(self.Snk_list)

        if self.Snk_list[ls - 1][0] == self.Snk_list[ls - 2][0]:
            if self.Snk_list[ls - 1][1] > self.Snk_list[ls - 2][1]:
                self.run(0, 1)
            else:
                self.run(0, -1)

        else:
            if self.Snk_list[ls - 1][0] > self.Snk_list[ls - 2][0]:
                self.run(1, 0)
            else:
                self.run(-1, 0)

        self.canvas.after(500, self.automatic_run)

    def game_over(self):
        self.canvas.create_text((canvas_w // 2), (canvas_h // 2), text='Game Over',font=70)
        qb = tkinter.Button(self, text='Quit', font=50, command=self.destroy)
        qb.grid(row=0)
        rb = tkinter.Button(self, text='Again', font=50, command=self.again)
        rb.grid(row=1)

    def again(self):
        self.destroy()
        self.__init__()

if __name__ == '__main__':

    win = Win(500, 600, 10)
    win.bind('<Key-Up>', win.move_up)
    win.bind('<Key-Down>', win.move_down)
    win.bind('<Key-Left>', win.move_left)
    win.bind('<Key-Right>', win.move_right)

    win.mainloop()
