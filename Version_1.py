

#When the program first runs it will display this message
print("""Welcome to the NBA Quiz!
There will be 10 Questions for you to answer.
""" )
#This will allow the user to start the quiz by typng y and exit with n
def menu():
    choice=input("Are you ready to start? (y/n):")
    return choice
#First question
def q1():
    #This allows users to input the answers and named it 'choice'
    choice=input("""What does "NBA" stand for?
    A. National Basketball Account
    B. Nation Basketball Associate
    C. National Basektball Association
    Option:""")
    #Giving what happens if depending on the option picked
    if choice =="C":
        print("Correct!")
        q2()
    else:
        print("Wrong Answer")
        q1()
#Second question
def q2():
    choice=input("""How many players on the court for each team during an NBA game?
    A. 6
    B. 5
    C. 10
    Option:""")
    if choice =="B":
        print("Correct!")
        q3()
    else:
        print("Wrong Answer")
        q2()
#Third Question
def q3():
    choice=input("""How many quarters are there in an NBA game?
    A. 3
    B. 4
    C. 2
    Option:""")
    if choice =="B":
        print("Correct!")
        q4()
    else:
        print("Wrong Answer")
        q3()
#fourth question
def q4():
    choice=input("""How many points is a three pointer worth?
    A. 3
    B. 2
    C. 3.5
    Option:""")
    if choice =="A":
        print("Correct!")
        q5()
    else:
        print("Wrong Answer")
        q4()
#fifth question
def q5():
    choice=input("""What is the name of the championship trophy?
    A. Larry O'Brien NBA Championship Trophy
    B. Season NBA Championship Trophy
    C. Michael Jordan NBA Championship Trophy
    Option:""")
    if choice =="A":
        print("Correct!")
        q6()
    else:
        print("Wrong Answer")
        q5()
#sixth question
def q6():
    choice=input("""How long is an NBA regulation game?
    A. 60 minutes
    B. 48 minutes
    C. 52 minutes
    Option:""")
    if choice =="B":
        print("Correct!")
        q7()
    else:
        print("Wrong Answer")
        q6()
#seventh question
def q7():
    choice=input("""Who is the NBA's logo modeled after?
    A. Michael Jordan
    B. Magic Johnson
    C. Jerry West
    Option:""")
    if choice =="C":
        print("Correct!")
        q8()
    else:
        print("Wrong Answer")
        q7()
#eighth quetion
def q8():
    choice=input("""What is the minimum age to be eligible for the NBA draft?
    A. 18
    B. 19
    C. 17
    Option:""")
    if choice =="B":
        print("Correct!")
        q9()
    else:
        print("Wrong Answer")
        q8()
#nineth question
def q9():
    choice=input("""What is the name of the NBA's All-Star Game MVP award?
    A. Kobe Bryant MVP Award
    B. All- Star Game MVP Award
    C. Best Player Award
    Option:""")
    if choice =="A":
        print("Correct!")
        q10()
    else:
        print("Wrong Answer")
        q9()
#Tenth question
def q10():
    while True:
        choice=input("""What is the name of the NBA's 3-point shooting contest held during All-Star Weekend?
    A. Sniper All-Star
    B. Best Shooter
    C. Three-Point Contest
    Option:""")
        if choice =="C":
            print("""Correct!
Quiz Finished! Good Job!""")
            break
            
        else:
            print("Wrong Answer")
            q10()       
#Main Routine
def main():
    while True:
        choice=menu()
        if choice == "y":
            q1()
        elif choice == "n":
            break
        else:
            print("Invalid Answer")
main()


    


