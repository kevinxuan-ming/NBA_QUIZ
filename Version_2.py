
print("""Welcome to the NBA Quiz!
There will be 10 Questions for you to answer.
""" )
#Naming Variables
score = 0
name = input("Enter Name:")
#The menu function
def menu():
    choice=input("Are you ready to start? (y/n):")
    return choice 
#Question 2
def q1():
    global score
    choice=input("""What does "NBA" stand for?
    A. National Basketball Account
    B. Nation Basketball Associate
    C. National Basektball Association
    Option:""")
    if choice =="C":
        print("Correct!")
        score = score + 1
        q2()
      
    else:
        print("Wrong Answer")
        q2()
#Question 2
def q2():
    global score
    choice=input("""How many players on the court for each team during an NBA game?
    A. 6
    B. 5
    C. 10
    Option:""")
    if choice =="B":
        print("Correct!")
        score = score + 1
        q3()
       
    else:
        print("Wrong Answer")
        q3()
#Question 3
def q3():
    global score
    choice=input("""How many quarters are there in an NBA game?
    A. 3
    B. 4
    C. 2
    Option:""")
    if choice =="B":
        print("Correct!")
        score = score + 1
        q4()
        
    else:
        print("Wrong Answer")
        q4()
#Question 4
def q4():
    global score
    choice=input("""How many points is a three pointer worth?
    A. 3
    B. 2
    C. 3.5
    Option:""")
    if choice =="A":
        print("Correct!")
        score = score + 1
        q5()
      
    else:
        print("Wrong Answer")
        q5()
#Question 5
def q5():
    global score
    choice=input("""What is the name of the championship trophy?
    A. Larry O'Brien NBA Championship Trophy
    B. Season NBA Championship Trophy
    C. Michael Jordan NBA Championship Trophy
    Option:""")
    if choice =="A":
        print("Correct!")
        score = score + 1
        q6()
        
    else:
        print("Wrong Answer")
        q6()
#Question 6
def q6():
    global score
    choice=input("""How long is an NBA regulation game?
    A. 60 minutes
    B. 48 minutes
    C. 52 minutes
    Option:""")
    if choice =="B":
        print("Correct!")
        score = score + 1
        q7()
       
    else:
        print("Wrong Answer")
        q7()
#Question 7
def q7():
    global score
    choice=input("""Who is the NBA's logo modeled after?
    A. Michael Jordan
    B. Magic Johnson
    C. Jerry West
    Option:""")
    if choice =="C":
        print("Correct!")
        score = score + 1
        q8()
       
    else:
        print("Wrong Answer")
        q8()
#Question 8
def q8():
    global score
    choice=input("""What is the minimum age to be eligible for the NBA draft?
    A. 18
    B. 19
    C. 17
    Option:""")
    if choice =="B":
        print("Correct!")
        score = score + 1       
        q9()
        #score = score + 1
    else:
        print("Wrong Answer")
        q9()
#Question 9
def q9():
    global score
    choice=input("""What is the name of the NBA's All-Star Game MVP award?
    A. Kobe Bryant MVP Award
    B. All- Star Game MVP Award
    C. Best Player Award
    Option:""")
    if choice =="A":
        print("Correct!")
        score = score + 1
        q10()
    else:
        print("Wrong Answer")
        q10()
#Question Ten
def q10():
    global score
    while True:
        choice=input("""What is the name of the NBA's 3-point shooting contest held during All-Star Weekend?
    A. Sniper All-Star
    B. Best Shooter
    C. Three-Point Contest
    Option:""")
        if choice =="C":
           
            print ("correct")
            score = score + 1
            mark()
            break   
        else:
            print("Wrong Answer")
            mark()
            break
#This helps print the users final score          
def mark():
#Global used to call variables outside the function
    global score
    global name
    while True:
        print("Well done "+str(name)+", you scored "+str(score)+"/10.")
        break         
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