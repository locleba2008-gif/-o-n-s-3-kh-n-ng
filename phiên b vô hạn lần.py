import random
a=random.randint(1,100)
while True:
    n=float(input())
    if n<a:
        print('nhỏ hơn')
    elif n==a:
        print('bằng')
    else:
        print('lớn hơn')        