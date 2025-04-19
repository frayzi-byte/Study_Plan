import random
ws = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
input('Choose password lenght from 6-12')
match(input):
    case "6":
        password = num1 + num2 + num3 + num4 + num5 + num6
    case "7":
        password = num1 + num2 + num3 + num4 + num5 + num6 + num7 
    case "8":
        password = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
    case "9":
        password = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
    case "10":
        password = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 +  num10
    case "11":
        password = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11
    case "12":
        password = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12
num1 = random.choice(ws)
num2 = random.choice(ws)
num3 = random.choice(ws)
num4 = random.choice(ws)
num5 = random.choice(ws)
num6 = random.choice(ws)
num7 = random.choice(ws)
num8 = random.choice(ws)
num9 = random.choice(ws)
num10 = random.choice(ws)
num11 = random.choice(ws)
num12 = random.choice(ws)
print(f"Password is:", password)