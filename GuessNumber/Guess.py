import random 
import math

def main():
    y = Myfunction('n')
    print(y)

def Myfunction(n):
    lower = int(input("Enter your lower: "))
    upper = int(input("Enter your upper: "))

    x = random.randint(lower, upper)
    return f"you have only {round(math.log(upper-lower+1,2))} chance to guess integer!"

    count = 0
    while count<math.log(upper-lower+1,2):
        count+=1
        guess = int(input("Guess a number: "))
        if x==guess:
            return f"Won!, {count} step"
            break
        elif x>guess:
            return "You guessed to small!"
        elif x<guess:
            return "you guessed to high!"

    if count>= math.log(upper-lower+1,2):
        return f"The number is {x} better luck next time!"
    
            
if __name__=='__main__':
    main()