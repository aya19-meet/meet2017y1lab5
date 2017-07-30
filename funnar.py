
def add_numbers(start,end):
    c=0
    for number in range(start,end+1,2):
        c=c+number
    return c

start = int(input('give me a number:? '))
end=int( input('give me another number:? '))

answer=add_numbers(start,end)
print(answer)





