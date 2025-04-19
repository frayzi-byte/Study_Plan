import random
while True:
    ws = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    lenght = input('Choose password lenght from 6-12\n')
    if lenght.isdigit() and 6 <= int(lenght) <= 12:
        password = ''.join(random.choice(ws) for _ in range(int(lenght)))
    print(f'Password is {password}')
else:
    print('Invalid input, please try again') 
    