import random
login = input('Login ')
password = ''
for x in range(11): #Количество символов (11)
    password = password + random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print('Hello, ', login, 'your password is: ', password)
