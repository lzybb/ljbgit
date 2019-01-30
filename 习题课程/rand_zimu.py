
class GameZiMu():
   def a(self):
      # 打印字母A
      for i in range(1,7):
         for k in range(7-i):
            print(' ',end='')
         for j in range(1,i+1):
            if i==1 or i==4 or j==1 or j==i:
               print('*',end=' ')
            else:
               print(' ',end=' ')
         print()

   def b(self):
      # 打印字母B
      for i in range(7):
         if i==0 or i==3 or i==6:
            for j in range(3):
               print('*',end=' ')
            print()
         else:
            for j in range(4):
               if j==0 or j==3:
                  print('*',end=' ')
               else:
                  print(' ',end=' ')
            print()

   def c(self):
      # 打印字母C
      for i in range(6):
         if i==0 or i==5:
            for j in range(4):
               if j>1:
                  print('*',end=' ')
               else:
                  print(' ',end=' ')
            print()
         if 0<i<=2:
            for j in range(4):
               if j==2-i:
                  print('*',end=' ')
               else:
                  print(' ',end=' ')
            print()
         if 2<i<5:
            for j in range(4):
               if j==i-3:
                  print('*',end=' ')
               else:
                  print(' ',end=' ')
            print()

   def d(self):
      # 打印字母D
      for i in range(6):
         if i==0 or i==5:
            for j in range(3):
               print('*',end=' ')
            print()
         if 0<i<=2:
            for j in range(5):
               if j==0 or j==i+2:
                  print('*',end=' ')
               else:
                  print(' ',end=' ')
            print()
         if 2<i<5:
            for j in range(5):
               if j==0 or j==7-i:
                  print('*',end=' ')
               else:
                  print(' ',end=' ')
            print()

   def e(self):
      for i in range(7):
         for j in range(5):
            if i==0 or i==3 or i==6 or j==0:
               print('*',end=' ')
            else:
               print(' ',end=' ')
         print()

   def f(self):
      for i in range(7):
         for j in range(5):
            if i==0 or i==3 or j==0:
               print('*',end=' ')
            else:
               print(' ',end=' ')
         print()
