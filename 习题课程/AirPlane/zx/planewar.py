import tkinter
import time
import configparser
import random


class Flyer():

    file_name = ''
    width = 0
    height = 0
    point_x = 0
    point_y = 0
    point = (0, 0)
    point_set = set()
    move_x = 0
    move_y = 0


    def p_set(self):
        w = (self.width)//2
        h = (self.height)//2
        for i in range(self.point_x-w, self.point_x+w+1):
            for j in range(self.point_y-h, self.point_y+h+1):
                p = (i, j)
                self.point_set.add(p)
        return self.point_set

    def move(self, move_x=0, move_y=1):
        if self.point_y > win_h:
            return False
        else:
            self.point_x = self.point_x + move_x
            self.point_y = self.point_y + move_y
            return True

class splane(Flyer):
    def __init__(self):
        self.file_name = '../img/plane1.gif'
        self.width = 49//px
        self.height = 36//px
        self.point_x = random.randint(5, win_w-5)
        self.point_y = -4





class bg():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def bg_move(self):
        if self.y < win_h*px + win_h*px//2:
            self.y += (win_h*px//100)
        else:
            self.y = self.y - 2*win_h*px
        return self.y




class Win():
    img_list = []

    def __init__(self):
        global cfg
        cfg = configparser.ConfigParser()
        cfg.read(filenames='plane_pm.cfg', encoding='utf-8')

        ############
        '''
        画布创作
        '''
        win_tk = tkinter.Tk()
        win_tk.title('李卓洋的飞机大战')
        win_tk.resizable(width=False, height=False)

        global px
        px = cfg.getint('canvas', 'pixel')
        global win_w
        win_w = cfg.getint('canvas', 'width')//px
        global win_h
        win_h = cfg.getint('canvas', 'height')//px


        global win_canvas
        win_canvas = tkinter.Canvas(win_tk, width=win_w*px, height=win_h*px)
        win_canvas.grid(row=1)
        ##############

        '''
        背景创作
        '''
        self.bg1 = bg(win_w*px//2, win_h*px//2)
        self.bg2 = bg(win_w*px//2, -win_h*px//2)

        self.b1 = 'b1'
        self.b1_img_name = '../img/background.gif'
        self.b1_img = tkinter.PhotoImage(file=self.b1_img_name)
        win_canvas.create_image(win_w*px//2, win_h*px//2, anchor=tkinter.CENTER, image=self.b1_img, tags=self.b1)

        self.b2 = 'b2'
        self.b2_img_name = '../img/background.gif'
        self.b2_img = tkinter.PhotoImage(file=self.b2_img_name)
        win_canvas.create_image(win_w*px//2, -win_h*px//2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.b2)

        #self.bg_run()
        # #########

        self.count = 0
        self.win_run()
        self.enemy_list = []
        self.img_list = []

        self.win_run()


        win_tk.mainloop()

    def bg_run(self):

        win_canvas.delete(self.b1)
        win_canvas.delete(self.b2)

        y1 = self.bg1.bg_move()
        y2 = self.bg2.bg_move()
        win_canvas.create_image(win_w*px//2, y1, anchor=tkinter.CENTER, image=self.b1_img, tags=self.bg1)
        win_canvas.create_image(win_w*px//2, y2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.bg2)

        win_canvas.after(150, self.bg_run)

    def enemy_produce(self):
        self.count %= 100000

        if self.count % 6 == 0:
            i = splane()
            img = tkinter.PhotoImage(file=i.file_name)
            j = win_canvas.create_image(i.point_x*px, i.point_y*px, anchor=tkinter.CENTER, image=img)
            self.img_list.append(j)
            self.enemy_list.append(i)



    def win_run(self):
        self.count += 1
        self.enemy_produce()

        if self.img_list != []:
            for i in self.img_list:
                win_canvas.delete(i)
            self.img_list = []

            new_enemy_list = []
            for j in self.enemy_list:
                isin = j.move()
                if isin == True:
                    new_enemy_list.append(j)
                else:
                    pass
            self.enemy_list = new_enemy_list
            for k in self.enemy_list:
                img = tkinter.PhotoImage(file=k.file_name)
                v = win_canvas.create_image(k.point_x*px, k.point_y*px, anchor=tkinter.CENTER, image=img)
                self.img_list.append(v)

        else:
            pass

        win_canvas.delete(self.b1)
        win_canvas.delete(self.b2)

        y1 = self.bg1.bg_move()
        y2 = self.bg2.bg_move()
        win_canvas.create_image(win_w*px//2, y1, anchor=tkinter.CENTER, image=self.b1_img, tags=self.bg1)
        win_canvas.create_image(win_w*px//2, y2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.bg2)



        win_canvas.after(150, self.win_run)








if __name__ == '__main__':
    win = Win()


