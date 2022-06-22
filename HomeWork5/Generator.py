import time


def gen_numbers():
    num = 0
    while True:
        time.sleep(1)
        num += 1
        yield num


gen = gen_numbers()
while True:
    i = (next(gen))
    if i % 3 == 0:
        a = i/3
        print('Василий ', i, ', остаток от делений => ', a)
    else:
        print(i)
