import time


def generator_numbers():
    number = 0
    while True:
        time.sleep(1)
        number += 1
        yield number


gen_numb = generator_numbers()
while True:
    buf1 = (next(gen_numb))
    if buf1 % 3 == 0:
        buf2 = buf1/3
        print('Василий ', buf1, ', остаток от делений => ', buf2)
    else:
        print(buf1)