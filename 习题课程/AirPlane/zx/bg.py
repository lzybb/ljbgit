import tkinter
import time
import threading

'''
所有的画面生成都需要在一个主程序里完成，不然会有问题
'''


class bg():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def bg_move(self):
        if self.y < win_h + win_h//2:
            self.y += (win_h//100)
        else:
            self.y = self.y - 2*win_h
        return self.y



class P_win():
    def __init__(self):
        global win_w
        win_w = 480
        global win_h
        win_h = 600

        global win
        win = tkinter.Tk()
        win.title('PlaneWar')
        win.resizable(width=False, height=False)

        global win_canvas
        win_canvas = tkinter.Canvas(win, width=win_w,height=win_h)
        win_canvas.grid(row=1)
        global x
        x = win_w//2
        self.bg1 = bg(x, win_h//2)
        self.bg2 = bg(x, -win_h//2)

        self.b1 = 'b1'
        self.b1_img_name = '../img/background.gif'
        self.b1_img = tkinter.PhotoImage(file=self.b1_img_name)
        win_canvas.create_image(x, win_h//2, anchor=tkinter.CENTER, image=self.b1_img, tags=self.b1)

        self.b2 = 'b2'
        self.b2_img_name = '../img/background.gif'
        self.b2_img = tkinter.PhotoImage(file=self.b2_img_name)
        win_canvas.create_image(x, -win_h//2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.b2)


        self.win_run()

        win.mainloop()
    def win_run(self):

        win_canvas.delete(self.b1)
        win_canvas.delete(self.b2)

        y1 = self.bg1.bg_move()
        y2 = self.bg2.bg_move()
        win_canvas.create_image(x, y1, anchor=tkinter.CENTER, image=self.b1_img, tags=self.bg1)
        win_canvas.create_image(x, y2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.bg2)

        win_canvas.after(150, self.win_run)




if __name__ == '__main__':
    p = P_win()


