import random
h = 0
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input('How many passwords?'+ "\n"))
length = int(input('How many simbols in password?'+ "\n"))
for n in range(number):
    h = h+1
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(h,' - ',password)
