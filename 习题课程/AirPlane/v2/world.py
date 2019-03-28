import tkinter
import time
import random as rd

'''
蜜蜂从上向下运动
可以通过键盘左右控制
'''
step = 0  # 计数器
direciton = (1,1)
x=0
y=10

def set_right(e):
    global x
    x = 10

def set_left(e):
    global x
    x = -10

root_window = tkinter.Tk()
root_window.title('飞机打蜜蜂')

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)

# 创建画布
window_canvas = tkinter.Canvas(root_window, width=480, height=600)
window_canvas.pack()

def main():
    # 创建开始界面
    bg_img_name = '../img/background.gif'
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER,
                               image=bg_img, tags='bg')

    sp_img_name = '../img/smallplane.gif'
    sp_img = tkinter.PhotoImage(file=sp_img_name)
    window_canvas.create_image(50, 50, anchor=tkinter.CENTER,
                               image=sp_img, tags='sp')

    # 让小飞机动起来
    ap_move()
    root_window.mainloop()


def ap_move():
    global step
    global x
    global y
    y = 6 + (step/50)*6
    print(x,y)
    window_canvas.move('sp',x,y) # Canvas.move 自带函数

    step +=1
    window_canvas.after(150,ap_move)



if __name__ == '__main__':
    main()
