
import tkinter
import random
import configparser


class Flyer():
    enemy_num = 0
    bullet_num = 0
    bg_num = 0
    hero_num = 0
    def move(self):
        if self.point_y > win_h - 2:
            return False
        else:
            self.point_x = self.point_x + self.move_x
            self.point_y = self.point_y + self.move_y
            self.point = (self.point_x, self.point_y)
            return self.point

class Smallplane(Flyer):
    def __init__(self):
        Flyer.enemy_num %= 100000
        Flyer.enemy_num += 1
        self.num = 'e' + str(Flyer.enemy_num)
        self.width = 49//px
        self.height = 36//px
        self.w = (self.width) // 2
        self.h = (self.height) // 2
        self.point_x = random.randint(5, win_w-5)
        self.point_y = -4
        self.point = (self.point_x, self.point_y)
        self.move_x = 0
        self.move_y = 1

class Bigplane(Flyer):
    def __init__(self):
        Flyer.enemy_num %= 100000
        Flyer.enemy_num += 1
        self.num = 'e' + str(Flyer.enemy_num)
        self.width = 69//px
        self.height = 99//px
        self.w = (self.width) // 2
        self.h = (self.height) // 2
        self.point_x = random.randint(7, win_w-7)
        self.point_y = -6
        self.point = (self.point_x, self.point_y)
        self.move_x = 0
        self.move_y = 2

class Bee(Flyer):
    def __init__(self):
        Flyer.enemy_num %= 100000
        Flyer.enemy_num += 1
        self.num = 'e' + str(Flyer.enemy_num)
        self.width = 60//px
        self.height = 50//px
        self.w = (self.width)//2
        self.h = (self.height)//2
        self.point_x = random.randint(7, win_w-7)
        self.point_y = -5
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
            return self.point




class Player():
    def __init__(self):
        self.num = str(0)
        self.width = 97//px
        self.height = 123//px
        self.point_x = win_w//2
        self.point_y = win_h - 20
        self.point = (self.point_x, self.point_y)

    def move(self, move_x=0, move_y=0):
        move_point_x = self.point_x + move_x
        move_point_y = self.point_y + move_y
        if move_point_x < 4 or move_point_x > win_w-4:
            pass
        elif move_point_y < 10 or move_point_y > win_h-10:
            pass
        else:
            self.point_x = move_point_x
            self.point_y = move_point_y
            self.point = (self.point_x, self.point_y)
        return self.point

class Bullet(Flyer):
    def __init__(self, h_pointx, h_pointy):
        Flyer.bullet_num %= 100000
        Flyer.bullet_num += 1
        self.num = 'b' + str(Flyer.bullet_num)
        self.width = 8//px
        self.height = 14//px
        self.point_x = h_pointx
        self.point_y = h_pointy - 10
        self.point = (self.point_x, self.point_y)
        self.move_x = 0
        self.move_y = -1
    def move(self):
        if self.point_y < 6:
            return False
        else:
            self.point_x = self.point_x + self.move_x
            self.point_y = self.point_y + self.move_y
            self.point = (self.point_x, self.point_y)
            return self.point


class Win(tkinter.Tk):
    def __init__(self):
        global cfg
        cfg = configparser.ConfigParser()
        cfg.read(filenames='plane_pm.cfg', encoding='utf-8')

        global px
        px = cfg.getint('canvas', 'pixel')
        global win_w
        win_w = cfg.getint('canvas', 'width')//px
        global win_h
        win_h = cfg.getint('canvas', 'height')//px

        tkinter.Tk.__init__(self)
        self.title('李卓洋的飞机大战')
        self.resizable(width=False, height=False)


        self.canvas = tkinter.Canvas(self, width=win_w*px, height=win_h*px)
        self.canvas.grid(row=0)

        self.small_img = tkinter.PhotoImage(file='../img/smallplane.gif')

        self.big_img = tkinter.PhotoImage(file='../img/bigplane.gif')

        self.bee_img = tkinter.PhotoImage(file='../img/bee.gif')

        self.hero_img = tkinter.PhotoImage(file='../img/hero.gif')

        self.bullet_img = tkinter.PhotoImage(file='../img/bullet.gif')

        self.count = 0
        self.enemy_list = list()
        self.bullet_list = list()


        self.h = 'hero'
        self.player = Player()
        self.canvas.create_image(self.player.point_x * px, self.player.point_y * px, anchor=tkinter.CENTER,
                                image=self.hero_img, tags=self.h)

        self.bind('<Key-Up>', self.move_up)
        self.bind('<Key-Down>', self.move_down)
        self.bind('<Key-Left>', self.move_left)
        self.bind('<Key-Right>', self.move_right)


        self.win_run()



        self.mainloop()


    def move_up(self, event):
        self.canvas.delete(self.h)
        self.player.move(0, -1)
        self.canvas.create_image(self.player.point_x * px, self.player.point_y * px, anchor=tkinter.CENTER,
                                image=self.hero_img, tags=self.h)
    def move_down(self, event):
        self.canvas.delete(self.h)
        self.player.move(0, 1)
        self.canvas.create_image(self.player.point_x * px, self.player.point_y * px, anchor=tkinter.CENTER,
                                 image=self.hero_img, tags=self.h)

    def move_left(self, event):
        self.canvas.delete(self.h)
        self.player.move(-1, 0)
        self.canvas.create_image(self.player.point_x * px, self.player.point_y * px, anchor=tkinter.CENTER,
                                 image=self.hero_img, tags=self.h)

    def move_right(self, event):
        self.canvas.delete(self.h)
        self.player.move(1, 0)
        self.canvas.create_image(self.player.point_x * px, self.player.point_y * px, anchor=tkinter.CENTER,
                                 image=self.hero_img, tags=self.h)

    def flyer_proudce(self):
        if self.count % 3 == 0:

            blt = Bullet(self.player.point_x, self.player.point_y)
            self.bullet_list.append(blt)
            self.canvas.create_image(blt.point_x*px, blt.point_y*px, anchor=tkinter.CENTER,
                                     image=self.bullet_img, tags=blt.num)

        if self.count % 12 == 0:
            s = Smallplane()
            self.enemy_list.append(s)
            self.canvas.create_image(s.point_x*px, s.point_y*px, anchor=tkinter.CENTER,
                                    image=self.small_img, tags=s.num)

        if self.count % 18 == 0:
            b = Bigplane()
            self.enemy_list.append(b)
            self.canvas.create_image(b.point_x*px, b.point_y*px, anchor=tkinter.CENTER,
                                    image=self.big_img, tags=b.num)

        if self.count % 24 == 0:
            bee = Bee()
            self.enemy_list.append(bee)
            self.canvas.create_image(bee.point_x*px, bee.point_y*px, anchor=tkinter.CENTER,
                                    image=self.bee_img, tags=bee.num)

    def hit(self):
        if len(self.enemy_list) == 0:
            pass
        else:
            del_enemys = set()
            del_bullets = set()
            for i in self.enemy_list:
                for j in self.bullet_list:
                    if i.point_x-i.w < j.point_x < i.point_x+i.w and i.point_y-i.h < j.point_y < i.point_y+i.h:
                        self.canvas.delete(i.num)
                        self.canvas.delete(j.num)
                        del_enemys.add(i)
                        del_bullets.add(j)
                        continue
                    else:
                        pass
            enemy_set = set(self.enemy_list)
            bullet_set = set(self.bullet_list)
            new_enemy_list = list(enemy_set-del_enemys)
            new_bullet_list = list(bullet_set-del_bullets)
            self.enemy_list = new_enemy_list
            self.bullet_list = new_bullet_list

    def flyer_run(self):

        if len(self.enemy_list) == 0:
            pass
        else:
            new_enemy_list = list()
            for i in self.enemy_list:
                j = i.move()
                self.canvas.move(i.num, i.move_x * px, i.move_y * px)
                if j == False:
                    self.canvas.delete(i.num)
                else:
                    new_enemy_list.append(i)
            self.enemy_list = new_enemy_list


        if len(self.bullet_list) == 0:
            pass
        else:
            new_bullet_list = list()
            for k in self.bullet_list:
                v = k.move()
                self.canvas.move(k.num, k.move_x*px, k.move_y * px)
                if v == False:
                    self.canvas.delete(k.num)
                else:
                    new_bullet_list.append(k)
            self.bullet_list = new_bullet_list



    def win_run(self):
        self.count %= 1000000
        self.count += 1

        self.flyer_proudce()
        self.hit()
        self.flyer_run()


        self.canvas.after(120, self.win_run)


if __name__ == '__main__':
    win = Win()
    print('all done')


