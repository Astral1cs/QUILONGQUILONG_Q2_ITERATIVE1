
def nega():
    age = int(input("input your age: "))
    while age <= 0 :
        print (f"Invalid age, must put an age that is greater than zero or not a decimal.")
        age = int(input("Please input your age: "))
    return age

def expectedbaby(age):
    check = age * (age + 1) / 2
    return check


def summity(age):
    sum = 0
    for i in range(1, age + 1):
        sum += 1
    return sum

age = nega()
Expectedsummity = expectedbaby(age)
actualsummity = summity(age)
Expecetedsummity = int(Expectedsummity)
actualsummity = int(actualsummity)




print (f"The expected output is {Expectedsummity}.")
print (f"After calling the function getSum, the sum of all numbers from 1 to {age} is {actualsummity}.")

if Expectedsummity == actualsummity:
    print ("Output verified!")