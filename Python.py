#programmed by imran sihab
from random import randint
print("Programmed by Imran Sihab\n")
print("Chose series:\n1. Addition Series\n2. Multiple Series\n3. Star Print\n4. Guessing Game\n5. Find Letter, Number or Digit")
ch = int(input("Enter number: "))

if ch==1:
    print("This is a addition series")
    n = int(input("Enter the last number: "))
    result = 0
    for x in range(1,n+1,1):
        result = result + x
    print(result)
    
elif ch==2:
    print("This is a multiply series")
    m = int(input("Enter the last number: "))
    result0 = 1
    for x in range(1,m+1,1):
        result0 = result0 * x
    print(result0)
    
elif ch==3:
    print("This is to print Priamid with *")
    n = int(input("Enter the number of line: "))
    for x in range(n+1):
        print(x*"*")
    
elif ch==4:
        for x in range(1,3):
            print("Guess a nummber 1 to 5 :D")
            n = int(input("Enter the number you gusse: "))
            randomNumber = randint(1,5)
    
            if n == randomNumber:
                print("You Win")
            elif n>5:
                print("Between 5 :(")
            else:
                print("You Loss")
            print("\nDo you want to know the number?\n1. Yes\n2. No\n3. Exit\n")
            zen = int(input("Yes or No: "))
            if zen == 1:
                print(randomNumber)
            elif zen == 2:
                print("Good Day")
            elif zen == 3:
                exit()
            else:
                print("Next time chose a right number")
        
elif ch==5:
    num_word = 0
    num_digit = 0
    num_letter = 0
    
    n = input("Enter your Paragraph here: ")    
    

    for x in n:
        x = x.lower()
        if x>='a' and x<='z':
            num_letter = num_letter + 1
        
        if x>='0' and x<='9':
            num_digit = num_digit + 1
        
        if x==' ':
            num_word = num_word + 1
    print("Number of word: ", num_word)
    print("Number of letter: ", num_letter)
    print("Number of digit: ", num_digit)
    
    

else:
    print("please chose the right one")