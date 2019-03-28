import tkinter
import random
import configparser

class Enemy():
    num = 0
    bg_num = 0
    width = 0
    height = 0
    point_x = 0
    point_y = 0
    point = (0, 0)
    point_set = set()
    img = ''
    def p_set(self):
        w = (self.width)//2
        h = (self.height)//2
        for i in range(self.point_x-w, self.point_x+w+1):
            for j in range(self.point_y-h, self.point_y+h+1):
                p = (i, j)
                self.point_set.add(p)
        return self.point_set
    def move(self):
        if self.point_y > win_h + 15:
            return False
        else:
            self.point_x = self.point_x + self.move_x
            self.point_y = self.point_y + self.move_y
            self.point = (self.point_x, self.point_y)
            win_canvas.move(self.num, self.move_x * px, self.move_y * px)
            return self.point

class Smallplane(Enemy):
    def __init__(self):
        Enemy.num %= 100000
        Enemy.num += 1
        self.num = Enemy.num
        self.width = 49//px
        self.height = 36//px
        self.file_name = '../img/smallplane.gif'
        self.point_x = random.randint(5, win_w-5)
        self.point_y = -4
        self.point = (self.point_x, self.point_y)
        self.move_x = 0
        self.move_y = 1




class Bigplane(Enemy):
    pass

class Bee(Enemy):
    pass

class Bullet():
    pass

class Hero():
    pass

class Background(Enemy):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Enemy.bg_num += 1
        self.bg_num = Enemy.bg_num
        self.file_name = '../img/background.gif'

    def move(self):
        if self.y < win_h*px + win_h*px//2:
            self.y += (win_h*px//100)
            win_canvas.move(self.bg_num, 0, win_h * px // 100)
        else:
            self.y = self.y - 2*win_h*px
            win_canvas.move(self.bg_num, 0, -2 * win_h * px)
        return self.y

class Win():
    def __init__(self):
        global cfg
        cfg = configparser.ConfigParser()
        cfg.read(filenames='plane_pm.cfg', encoding='utf-8')

        global win_tk
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

        self.count = 0
        self.enemy_list = list()

        self.bg_produce()


        self.win_run()

        win_tk.mainloop()








    def bg_produce(self):

        bg1 = Background(win_w*px//2, win_h*px//2)
        bg2 = Background(win_w*px//2, -win_h*px//2)


        bg1_img = tkinter.PhotoImage(file=bg1.file_name)
        win_canvas.create_image(bg1.x, bg1.y, anchor=tkinter.CENTER,
                                image=bg1_img, tags=bg1.bg_num)

        bg2_img = tkinter.PhotoImage(file=bg2.file_name)
        win_canvas.create_image(bg2.x, bg2.y, anchor=tkinter.CENTER,
                                image=bg2_img, tags=bg2.bg_num)

        self.enemy_list.append(bg1)
        self.enemy_list.append(bg2)



    def enemy_produce(self):
        self.count %= 1000000
        if self.count % 8 == 0:
            i = Smallplane()
            self.enemy_list.append(i)

            i.img = tkinter.PhotoImage(file=i.file_name)
            win_canvas.create_image(i.point_x * px, i.point_y * px,
                                    anchor=tkinter.CENTER, image=i.img,
                                    tags=i.num)



    def enemy_move(self):
        new_enemy_list = list()
        for i in self.enemy_list:
            j = i.move()
            if j == False:
                win_canvas.delete(i.num)
            else:
                new_enemy_list.append(i)
            self.enemy_list = new_enemy_list

    def win_run(self):

        #self.bg_run()
        self.count +=1

        #self.enemy_produce()
        self.enemy_move()




        win_canvas.after(150, self.win_run)



if __name__ == '__main__':
    win = Win()
    print('all done')
