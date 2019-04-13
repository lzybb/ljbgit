import tkinter
import configparser

cfg = configparser.ConfigParser()
cfg.read(filenames='food_parameter.cfg', encoding='utf-8')

class Food():
    name = ''
    price = 0
    is_sell = False
    is_special = False
    #point_x = 0
    point_y = 0
    move_y = 4
    food_num = 0
    def move(self):
        self.point_y -= self.move_y

class Tomato(Food):  # 番茄
    def __init__(self):
        self.name = cfg.get('tomato', 'name')
        self.price = cfg.get('tomato', 'price')
        self.is_sell = cfg.get('tomato', 'is_sell')
        self.is_special = cfg.get('tomato', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Eggplant(Food): # 茄子
    def __init__(self):
        self.name = cfg.get('eggplant', 'name')
        self.price = cfg.get('eggplant', 'price')
        self.is_sell = cfg.get('eggplant', 'is_sell')
        self.is_special = cfg.get('eggplant', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Cucumber(Food): # 黄瓜
    def __init__(self):
        self.name = cfg.get('cucumber', 'name')
        self.price = cfg.get('cucumber', 'price')
        self.is_sell = cfg.get('cucumber', 'is_sell')
        self.is_special = cfg.get('cucumber', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Greens(Food): # 青菜
    def __init__(self):
        self.name = cfg.get('greens', 'name')
        self.price = cfg.get('greens', 'price')
        self.is_sell = cfg.get('greens', 'is_sell')
        self.is_special = cfg.get('greens', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Potato(Food): # 土豆
    def __init__(self):
        self.name = cfg.get('potato', 'name')
        self.price = cfg.get('potato', 'price')
        self.is_sell = cfg.get('potato', 'is_sell')
        self.is_special = cfg.get('potato', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Pumpkin(Food): # 南瓜
    def __init__(self):
        self.name = cfg.get('pumpkin', 'name')
        self.price = cfg.get('pumpkin', 'price')
        self.is_sell = cfg.get('pumpkin', 'is_sell')
        self.is_special = cfg.get('pumpkin', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Leek(Food): # 韭菜
    def __init__(self):
        self.name = cfg.get('leek', 'name')
        self.price = cfg.get('leek', 'price')
        self.is_sell = cfg.get('leek', 'is_sell')
        self.is_special = cfg.get('leek', 'is_special')
        Food.food_num %= 100000
        Food.food_num += 1
        self.num1 = 'f' + str(Food.food_num) + 'a'
        self.num2 = 'f' + str(Food.food_num) + 'b'

class Win(tkinter.Tk):
    def __init__(self):
        global px
        px = 10
        global win_w
        win_w = 860//px
        global win_h
        win_h = 300//px

        tkinter.Tk.__init__(self)  # 将TK()类的属性添加给Win()的子类
        self.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self, width=win_w*px, height=win_h*px)
        self.canvas.grid(row=0)
        # 左边
        self.canvas.create_text(1*px, 3*px, text='今日菜价', font=('黑体', 22, 'bold'),
                                fill='gray', anchor=tkinter.W)
        self.canvas.create_text(1*px, 7*px, text='菜名', font=('宋体', 18, 'bold'),
                                fill='gray', anchor=tkinter.W)
        self.canvas.create_text(16*px, 7*px, text='价格(元/斤)', font=('宋体', 18, 'bold'),
                                fill='gray', anchor=tkinter.W)

        # 右边
        self.canvas.create_text((win_w//2+1)*px, 3*px, text='今日特价菜', font=('黑体', 22, 'bold'),
                                fill='gray', anchor=tkinter.W)
        self.canvas.create_text((win_w//2+1)*px, 7*px, text='菜名', font=('宋体', 18, 'bold'),
                                fill='gray', anchor=tkinter.W)
        self.canvas.create_text((win_w//2+16)*px, 7*px, text='价格(元/斤)', font=('宋体', 18, 'bold'),
                                fill='gray', anchor=tkinter.W)

        self.sell_list = list()
        self.special_list = list()

        self.sell_food()

        self.win_run()

        self.mainloop()

    def sell_food(self):
        self.tomato = Tomato()
        if self.tomato.is_special == 'True':
            self.special_list.append(self.tomato)
        elif self.tomato.is_sell == 'True':
            self.sell_list.append(self.tomato)
        else:
            pass

        self.eggplant = Eggplant()
        if self.eggplant.is_special == 'True':
            self.special_list.append(self.eggplant)
        elif self.eggplant.is_sell == 'True':
            self.sell_list.append(self.eggplant)
        else:
            pass

        self.cucumber = Cucumber()
        if self.cucumber.is_special == 'True':
            self.special_list.append(self.cucumber)
        elif self.cucumber.is_sell == 'True':
            self.sell_list.append(self.cucumber)
        else:
            pass

        self.greens = Greens()
        if self.greens.is_special == 'True':
            self.special_list.append(self.greens)
        elif self.greens.is_sell == 'True':
            self.sell_list.append(self.greens)
        else:
            pass

        self.potato = Potato()
        if self.potato.is_special == 'True':
            self.special_list.append(self.potato)
        elif self.potato.is_sell == 'True':
            self.sell_list.append(self.potato)
        else:
            pass

        self.pumpkin = Pumpkin()
        if self.pumpkin.is_special == 'True':
            self.special_list.append(self.pumpkin)
        elif self.pumpkin.is_sell == 'True':
            self.sell_list.append(self.pumpkin)
        else:
            pass

        self.leek = Leek()
        if self.leek.is_special == 'True':
            self.special_list.append(self.leek)
        elif self.leek.is_sell == 'True':
            self.sell_list.append(self.leek)
        else:
            pass


        self.len_sell = len(self.sell_list)
        self.len_special = len(self.special_list)
        '''  
        下面是将列表信息初始化显示出来
        '''
        if self.len_sell == 0:
            pass
        elif 1 <= self.len_sell <= 5:
            a = 0
            for b in self.sell_list:
                self.canvas.create_text(1 * px, (11+a) * px, text=b.name, font=('宋体', 18, 'bold'),
                                        fill='green', anchor=tkinter.W, tags=b.num1)
                self.canvas.create_text(16 * px, (11+a) * px, text=b.price, font=('宋体', 18, 'bold'),
                                        fill='green', anchor=tkinter.W, tags=b.num2)
                a += 4
        else:
            c = 0
            for d in range(self.len_sell):
                self.sell_list[d].point_y = 11 + c
                if d < 5:
                    self.canvas.create_text(1*px, (11+c)*px, text=self.sell_list[d].name, font=('宋体', 18, 'bold'),
                                            fill='green', anchor=tkinter.W, tags=self.sell_list[d].num1)
                    self.canvas.create_text(16*px, (11+c)*px, text=self.sell_list[d].price, font=('宋体', 18, 'bold'),
                                            fill='green', anchor=tkinter.W, tags=self.sell_list[d].num2)
                else:
                    pass
                c += 4

        if self.len_special == 0:
            pass
        elif 1 <= self.len_special <= 5:
            e = 0
            for f in self.special_list:
                self.canvas.create_text((win_w//2+1)*px, (11+e)*px, text=f.name, font=('宋体', 18, 'bold'),
                                        fill='red', anchor=tkinter.W)
                self.canvas.create_text((win_w//2+16)*px, (11+e)*px, text=f.price, font=('宋体', 18, 'bold'),
                                        fill='red', anchor=tkinter.W)
                e += 4
        else:
            i = 0
            for j in range(self.len_special):
                self.special_list[j].point_y = 11 + i
                if j < 5:
                    self.canvas.create_text((win_w//2+1)*px, (11+i)*px, text=self.special_list[j].name,
                                            font=('宋体', 18, 'bold'), fill='red', anchor=tkinter.W,
                                            tags=self.special_list[j].num1)
                    self.canvas.create_text((win_w//2+16)*px, (11+i)*px, text=self.special_list[j].price,
                                            font=('宋体', 18, 'bold'), fill='red', anchor=tkinter.W,
                                            tags=self.special_list[j].num2)
                else:
                    pass
                i += 4

    def win_run(self):

        if self.len_sell <= 5:
            pass
        else:
            for j in self.sell_list:
                self.canvas.delete(j.num1, j.num2)
                j.move()
                if j.point_y < 11:
                    j.point_y += (self.len_sell * 4)
                elif 11 <= j.point_y <= 11+4*4:
                    self.canvas.create_text(1*px, j.point_y*px, text=j.name, font=('宋体', 18, 'bold'),
                                            fill='green', anchor=tkinter.W, tags=j.num1)
                    self.canvas.create_text(16*px, j.point_y*px, text=j.price, font=('宋体', 18, 'bold'),
                                            fill='green', anchor=tkinter.W, tags=j.num2)
                else:
                    pass


        if self.len_special <= 5:
            pass
        else:
            for i in self.special_list:
                self.canvas.delete(i.num1, i.num2)
                i.move()
                if i.point_y < 11:
                    i.point_y += (self.len_special * 4)
                elif 11 <= i.point_y <= 11+4*4:
                    self.canvas.create_text((win_w//2+1)*px, i.point_y*px, text=i.name, font=('宋体', 18, 'bold'),
                                            fill='red', anchor=tkinter.W, tags=i.num1)
                    self.canvas.create_text((win_w//2+16)*px, i.point_y*px, text=i.price, font=('宋体', 18, 'bold'),
                                            fill='red', anchor=tkinter.W, tags=i.num2)
                else:
                    pass

        self.canvas.after(1500, self.win_run)

if __name__ == '__main__':
    win = Win()
