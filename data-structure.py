def work():
    status=input('are you married? ')
    age=int(input('how old are you?: '))
    name=input('whats your name?: ')

    print(f'my name is {name} and {status} am married and am {age}')
work()    

def add(n1,n2,n3):
    message= n1+n2-n3
    return message

number_one=int(input("enter your fist number:"))
number_two=int(input("enter your second number: "))
number_three=int(input("enter your third number:" ))
print(add(number_one,number_two,number_three))
