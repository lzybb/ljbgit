# 作业：
# 此屏保程序扩展成，一旦捕获事件，则判断屏保不退出
# 显示一个Button,Button上显示事件类型，点击Button后屏保才退出
import tkinter
import random


class rball():  # 定义球类
    def __init__(self, canvas, canvas_w, canvas_h):
        # 接收画板的信息
        self.canvas = canvas
        self.canvas_w = canvas_w
        self.canvas_h = canvas_h
        # 先定义球的大小
        self.radius = random.randint(20, 120)
        # 定义球的起始位置
        # 范围定义注意：不能球一出来就不完整
        self.xpos = random.randint(self.radius, (self.canvas_w - self.radius))
        self.ypos = random.randint(self.radius, (self.canvas_h - self.radius))
        # 定义球移动的大小
        self.xmove = random.randint(5, 25)
        self.ymove = random.randint(5, 25)
        # 造球：此处与讲义有区别
        # 此处没有另外定义造球函数，直接实例一个类定义一个球，逻辑会清晰一点
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())
        self.color1 = '#%02x%02x%02x' % (c(), c(), c())
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color1)

    def move_ball(self):  # 球动起来
        self.xpos += self.xmove
        self.ypos += self.ymove
        if (self.xpos - self.radius) <= 0 or (self.xpos + self.radius) >= self.canvas_w:
            self.xmove *= -1
        elif (self.ypos - self.radius) <= 0 or (self.ypos + self.radius) >= self.canvas_h:
            self.ymove *= -1
        self.canvas.move(self.item, self.xmove, self.ymove)


class ScreenSaver():
    balls = list()

    def __init__(self):
        # 先造个窗口
        self.win_dow = tkinter.Tk()
        # 去边框
        self.win_dow.overrideredirect(1)
        # 取屏幕的长宽值
        w = self.win_dow.winfo_screenwidth()
        h = self.win_dow.winfo_screenheight()
        # 将窗口都显示为画板
        self.canvas = tkinter.Canvas(self.win_dow, width=w, height=h)
        self.canvas.pack()
        # 准备画圆，数量随机
        self.balls_num = random.randint(10, 25)
        # 造的多个圆，并让外部参数接受，方便后面函数调用
        for i in range(self.balls_num):
            ball = rball(self.canvas, w, h)
            self.balls.append(ball)
        # 屏保调用自动让球动起来
        self.run_saver()

        # 捕捉系统事件:1,鼠标；2，键盘
        self.win_dow.bind('<Button-1>', self.levent1)
        self.win_dow.bind('<Key>', self.levent2)

        self.win_dow.mainloop()

    def run_saver(self):
        for ball in self.balls:
            ball.move_ball()
        # 每隔多长时间，动一次(调用一次此函数)
        self.canvas.after(200, self.run_saver)

    def levent1(self, event):
        self.win1 = tkinter.Tk()
        self.btn = tkinter.Button(self.win1, text='鼠标事件', font=26, command=self.ljbquit)
        self.btn.pack()
        self.win1.mainloop()

    def levent2(self, event):
        self.win1 = tkinter.Tk()
        self.btn = tkinter.Button(self.win1, text='键盘事件', font=26, command=self.ljbquit)
        self.btn.pack()
        self.win1.mainloop()

    def ljbquit(self):
        self.win_dow.destroy()


if __name__ == '__main__':
    ScreenSaver()







