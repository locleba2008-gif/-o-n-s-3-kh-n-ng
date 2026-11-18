import random
a=random.randint(1,100)
i=1
while i<=7:
    n=float(input())
    if n<a:
        print('nhỏ hơn')
    elif n==a:
        print('bằng')
        break
    else:
        print('lớn hơn')      
    i+=1
if i==8 and n!=a:
    print('thua')
print('người chơi có muốn chơi lại không')
                 