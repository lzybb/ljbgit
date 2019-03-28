import tkinter
import random
import configparser

class Enemy():
    num = 0
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
        if self.point_y > win_h - 2:
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
    def __init__(self):
        Enemy.num %= 100000
        Enemy.num += 1
        self.num = Enemy.num
        self.width = 69//px
        self.height = 99//px
        self.file_name = '../img/bigplane.gif'
        self.point_x = random.randint(7, win_w-7)
        self.point_y = -4
        self.point = (self.point_x, self.point_y)
        self.move_x = 0
        self.move_y = 2


class Bee(Enemy):
    def __init__(self):
        Enemy.num %= 100000
        Enemy.num += 1
        self.num = Enemy.num
        self.width = 60//px
        self.height = 50//px
        self.file_name = '../img/bee.gif'
        self.point_x = random.randint(7, win_w-7)
        self.point_y = -4
        self.point = (self.point_x, self.point_y)
        self.move_x = random.choice([1, -1])
        self.move_y = 1

    def move(self):
        if self.point_y > win_h - 2:
            return False
        else:
            if self.point_x < 5 or self.point_x > win_w - 5:
                self.move_x *= -1
            self.point_x = self.point_x + self.move_x
            self.point_y = self.point_y + self.move_y
            self.point = (self.point_x, self.point_y)
            win_canvas.move(self.num, self.move_x * px, self.move_y * px)
            return self.point

class Hero():
    def __init__(self):
        self.num = 'hero'
        self.width = 97//px
        self.height = 124//px
        self.file_name = '../img/hero.gif'
        self.img = ''
        self.point_x = win_w//2
        self.point_y = win_h - 20
        self.point = (self.point_x, self.point_y)

    def hero_move(self, move_x=0, move_y=0):
        move_point_x = self.point_x + move_x
        move_point_y = self.point_y + move_y
        if move_point_x < 8 or move_point_x > win_w-8:
            pass
        elif move_point_y < 10 or move_point_y > win_h-10:
            pass
        else:
            self.point_x = move_point_x
            self.point_y = move_point_y
            self.point = (self.point_x, self.point_y)
            win_canvas.move(self.num, move_x * px, move_y * px)


class Bullet():
    pass

class Background():
    def __init__(self, x, y):
        self.point_x = win_w//2
        self.point_y = y
        self.file_name = '../img/background.gif'
        self.move_y = 1

    def move(self):
        if self.point_y < win_h + win_h//2:
            self.point_y += self.move_y
            win_canvas.move(self.num, 0, self.move_y*px)
        else:
            self.point_y = self.point_y - 2*win_h*px
            win_canvas.move(self.num, 0, -2*win_h*px)
        return self.point_y

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
        '''
        self.hero = Hero()

        self.hero.img = tkinter.PhotoImage(file=self.hero.file_name)
        win_canvas.create_image(self.hero.point_x * px, self.hero.point_y * px,
                                anchor=tkinter.CENTER, image=self.hero.img, tags=self.hero.num)
        '''


        win_tk.mainloop()



    def bg_produce(self):

        self.bg1 = Background(win_w*px//2, win_h*px//2)
        self.bg2 = Background(win_w*px//2, -win_h*px//2)

        self.b1 = 'b1'
        self.b1_img_name = '../img/background.gif'
        self.b1_img = tkinter.PhotoImage(file=self.b1_img_name)
        win_canvas.create_image(win_w*px//2, win_h*px//2, anchor=tkinter.CENTER, image=self.b1_img, tags=self.b1)

        self.b2 = 'b2'
        self.b2_img_name = '../img/background.gif'
        self.b2_img = tkinter.PhotoImage(file=self.b2_img_name)
        win_canvas.create_image(win_w*px//2, -win_h*px//2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.b2)

    def bg_run(self):
        '''
        win_canvas.delete(self.b1)
        win_canvas.delete(self.b2)

        y1 = self.bg1.bg_move()
        y2 = self.bg2.bg_move()
        win_canvas.create_image(win_w*px//2, y1, anchor=tkinter.CENTER, image=self.b1_img, tags=self.b1)
        win_canvas.create_image(win_w*px//2, y2, anchor=tkinter.CENTER, image=self.b2_img, tags=self.b2)
        '''
        if self.bg1.y < win_h*px + win_h*px//2:
            self.bg1.y += win_h*px//100
            win_canvas.move(self.b1, 0, win_h*px//100)
        else:
            self.bg1.y += -2*win_h*px
            win_canvas.move(self.b1, 0, -2*win_h*px)

        if self.bg2.y < win_h * px + win_h * px // 2:
            self.bg2.y += win_h*px//100
            win_canvas.move(self.b2, 0, win_h*px//100)
        else:
            self.bg2.y += -2 * win_h * px
            win_canvas.move(self.b2, 0, -2 * win_h * px)

        #win_canvas.after(180, self.bg_run)


    def enemy_produce(self):
        self.count %= 1000000
        if self.count % 12 == 0:
            i = Smallplane()
            self.enemy_list.append(i)
            i.img = tkinter.PhotoImage(file=i.file_name)
            win_canvas.create_image(i.point_x * px, i.point_y * px,
                                    anchor=tkinter.CENTER, image=i.img, tags=i.num)
        elif self.count % 18 == 0:
            i = Bigplane()
            self.enemy_list.append(i)
            i.img = tkinter.PhotoImage(file=i.file_name)
            win_canvas.create_image(i.point_x * px, i.point_y * px,
                                    anchor=tkinter.CENTER, image=i.img, tags=i.num)

        elif self.count % 26 == 0:
            i = Bee()
            self.enemy_list.append(i)
            i.img = tkinter.PhotoImage(file=i.file_name)
            win_canvas.create_image(i.point_x * px, i.point_y * px,
                                    anchor=tkinter.CENTER, image=i.img, tags=i.num)

    def enemy_move(self):
        if len(self.enemy_list) == 0:
            pass
        else:
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
        self.count += 1

        self.enemy_produce()
        self.enemy_move()




        win_canvas.after(150, self.win_run)



if __name__ == '__main__':
    win = Win()
    print('all done')

