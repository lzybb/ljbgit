import rand_zimu
import rand_math

print('请选择游戏\n1.数字游戏\n2.字母游戏')
game = input('请输入1或2：')
if game=='1':
    cs = 0
    df = 0
    game_num = rand_math.GameNum()
    game_num.num_game(cs,df)
elif game=='2':
    game_zimu = rand_zimu.GameZiMu()
    while 1:
        z = input('请输入一个字母，范围为（A-F），输入-1结束：')
        if z == '-1':
            break
        if z == 'A':
            game_zimu.a()
        if z == 'B':
            game_zimu.b()
        if z == 'C':
            game_zimu.c()
        if z == 'D':
            game_zimu.d()
        if z == 'E':
            game_zimu.e()
        if z == 'F':
            game_zimu.f()
        else:
            print('请按规则输入')

else:
    print('请按规则输入')

