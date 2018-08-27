print("\nhello world!")
print('{0:^20}'.format('hello'))
number = 23
running = False
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
# 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
# 在这里你可以做你想做的任何事
print('Done')


for i in range(1, 10):
    print(i)
    
else:
    print('the for loop is done')
    

    
while False:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
else:
    print('while else ')
print('Done')

a=5
#定义say_hello()函数
def say_hello():
    b =6
    print('hello world!ha ha ha ' ,a)
    
say_hello()
say_hello()
say_hello()

#定义say_hello()函数
def say(message, times):
    print(message * times)

say('Hello',2)
say(3, 'Hello')




def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。
    
    The two values must be integers.这两个数都应该是整数'''
# 如果可能，将其转换至整数类型

    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
#print(print_max.__doc__)

#help(print_max)

#import os
#print(os.getcwd())

mylist = ['Brazil', 'Russia', 'India', 'China']
JOIN=' #$%'
print(JOIN.join(mylist))










