
def add_numbers():
    c=0
    for number in range(num1, num2):
        c=c+number
        return c

num1 = int(input('give me a number:? '))
num2 = int( input('give me another number:? '))

answer=add_numbers(num1,num2)
print(answer)




