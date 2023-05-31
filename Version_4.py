#Allows us to use tkinter widgets
from tkinter import *  
import os
import sys
#Question 2
def frame3():
    global score
    global first_page2
    #if answers correct adds 1 to the varible 'score'
    if entry1.get() =="C":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame3
    global entry3
    first_page2 = Toplevel()
    first_page2.geometry("500x500+100+100")
    first_page2.title("NBA Question 2")
    frame3 = Frame(first_page2)
    frame3.grid(row=0,column=0, sticky='nsew')
    lblquestion=Label(frame3,text="""How many players on the court
      for each team during an NBA game?
    A. 6
    B. 5
    C. 10""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame3,text="Option:")
    lbloption.grid(row=1,column=0)
    entry3=Entry(frame3)
    entry3.grid(row=1,column=1)
    btn1=Button(frame3,text="Enter",command=frame4)
    btn1.grid(row=2,column=1)
    reset_button2=Button(frame3,text="Reset Quiz",command=lambda: reset_quiz(first_page2))
    reset_button2.grid(row=3,column=1)
    retry_button = Button(frame3, text="Retry Question", command=lambda: retry(first_page, first_page2))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame3,text="Skip Question",command=frame4)
    skip_button.grid(row=5,column=1)
    first_page.withdraw()
#Question 3
def frame4():
    global first_page3
    global score
    if entry3.get() =="B":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame4
    global entry4 
    global first_page3 
    first_page3 = Toplevel()
    first_page3.geometry("500x500+100+100")
    frame4 = Frame(first_page3)
    frame4.grid(row=0,column=0, sticky='nsew')
    first_page3.title("NBA Question 3")
    lblquestion=Label(frame4,text="""How many quarters are
    there in an NBA game?
    A. 3
    B. 4
    C. 2""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame4,text="Option:")
    lbloption.grid(row=1,column=0)
    entry4=Entry(frame4)
    entry4.grid(row=1,column=1)
    btn1=Button(frame4,text="Enter",command=frame5)
    btn1.grid(row=2,column=1)
    reset_button3=Button(frame4,text="Reset Quiz",command=lambda: reset_quiz(first_page3))
    reset_button3.grid(row=3,column=1)
    retry_button = Button(frame4, text="Retry Question", command=lambda: retry(first_page2, first_page3))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame4,text="Skip Question",command=frame5)
    skip_button.grid(row=5,column=1)
    first_page2.withdraw()
#Question 4
def frame5():
    global first_page4
    global score
    if entry4.get() =="B":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame5
    global entry5
    first_page4 = Toplevel()
    first_page4.geometry("500x500+100+100")
    frame5 = Frame(first_page4)
    frame5.grid(row=0,column=0, sticky='nsew')
    first_page4.title("NBA Question 4")
    lblquestion=Label(frame5,text="""How many points is a
    three pointer worth?
    A. 3
    B. 2
    C. 3.5""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame5,text="Option:")
    lbloption.grid(row=1,column=0)
    entry5=Entry(frame5)
    entry5.grid(row=1,column=1)
    btn1=Button(frame5,text="Enter",command=frame6)
    btn1.grid(row=2,column=1)
    reset_button4=Button(frame5,text="Reset Quiz",command=lambda: reset_quiz(first_page4))
    reset_button4.grid(row=3,column=1)
    retry_button = Button(frame5, text="Retry Question", command=lambda: retry(first_page3, first_page4))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame5,text="Skip Question",command=frame6)
    skip_button.grid(row=5,column=1)
    first_page3.withdraw()
#Question 5
def frame6():
    global score
    global first_page5

    if entry5.get() =="A":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame6
    global entry6
    first_page5 = Toplevel()
    first_page5.geometry("500x500+100+100")
    frame6 = Frame(first_page5)
    frame6.grid(row=0,column=0, sticky='nsew')
    first_page5.title("NBA Question 5")
    lblquestion=Label(frame6,text="""What is the name of the NBA's 
    3-point shooting contest held during All-Star Weekend?
    A. Sniper All-Star
    B. Best Shooter
    C. Three-Point Contest""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame6,text="Option:")
    lbloption.grid(row=1,column=0)
    entry6=Entry(frame6)
    entry6.grid(row=1,column=1)
    btn1=Button(frame6,text="Enter",command=frame7)
    btn1.grid(row=2,column=1)
    reset_button5=Button(frame6,text="Reset Quiz",command=lambda: reset_quiz(first_page5))
    reset_button5.grid(row=3,column=1)
    retry_button = Button(frame6, text="Retry Question", command=lambda: retry(first_page4, first_page5))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame6,text="Skip Question",command=frame7)
    skip_button.grid(row=5,column=1)
    first_page4.withdraw()
#Question 6   
def frame7():
    global score
    global first_page6
    if entry6.get() =="C":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame7
    global entry7
    first_page6 = Toplevel()
    first_page6.geometry("500x500+100+100")
    frame7 = Frame(first_page6)
    frame7.grid(row=0,column=0, sticky='nsew')
    first_page6.title("NBA Question 6")
    lblquestion=Label(frame7,text="""What is the name of the 
    championship trophy?
    A. Larry O'Brien NBA Championship Trophy
    B. Season NBA Championship Trophy
    C. Michael Jordan NBA Championship Trophy""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame7,text="Option:")
    lbloption.grid(row=1,column=0)
    entry7=Entry(frame7)
    entry7.grid(row=1,column=1)
    btn1=Button(frame7,text="Enter",command=frame8)
    btn1.grid(row=2,column=1)
    reset_button6=Button(frame7,text="Reset Quiz",command=lambda: reset_quiz(first_page6))
    reset_button6.grid(row=3,column=1)
    retry_button = Button(frame7, text="Retry Question", command=lambda: retry(first_page5, first_page6))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame7,text="Skip Question",command=frame8)
    skip_button.grid(row=5,column=1)
    first_page5.withdraw()
#Question 7  
def frame8():
    global score
    global first_page7
    if entry7.get() =="A":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global entry8
    global frame8
    first_page7 = Toplevel()
    first_page7.geometry("500x500+100+100")
    frame8 = Frame(first_page7)
    frame8.grid(row=0,column=0, sticky='nsew')
    first_page7.title("NBA Question 7")
    lblquestion=Label(frame8,text="""Who is the NBA's logo modeled after?
    A. Michael Jordan
    B. Magic Johnson
    C. Jerry West""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame8,text="Option:")
    lbloption.grid(row=1,column=0)
    entry8=Entry(frame8)
    entry8.grid(row=1,column=1)
    btn1=Button(frame8,text="Enter",command=frame9)
    btn1.grid(row=2,column=1)
    reset_button7=Button(frame8,text="Reset Quiz",command=lambda: reset_quiz(first_page7))
    reset_button7.grid(row=3,column=1)
    retry_button = Button(frame8, text="Retry Question", command=lambda: retry(first_page6, first_page7))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame8,text="Skip Question",command=frame9)
    skip_button.grid(row=5,column=1)
    first_page6.withdraw()
#Question 8 
def frame9():
    global score
    global first_page8
    if entry8.get() =="C":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global entry9
    global frame9
 
    first_page8 = Toplevel()
    first_page8.geometry("500x500+100+100")
    frame9 = Frame(first_page8)
    frame9.grid(row=0,column=0, sticky='nsew')
    first_page8.title("NBA Question 8")
    lblquestion=Label(frame9,text="""How long is an NBA regulation game?
    A. 60 minutes
    B. 48 minutes
    C. 52 minutes""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame9,text="Option:")
    lbloption.grid(row=1,column=0)
    entry9=Entry(frame9)
    entry9.grid(row=1,column=1)
    btn1=Button(frame9,text="Enter",command=frame10)
    btn1.grid(row=2,column=1)
    reset_button8=Button(frame9,text="Reset Quiz",command=lambda: reset_quiz(first_page8))
    reset_button8.grid(row=3,column=1)
    retry_button = Button(frame9, text="Retry Question", command=lambda: retry(first_page7, first_page8))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame9,text="Skip Question",command=frame10)
    skip_button.grid(row=5,column=1)
    first_page7.withdraw()
#Question 9
def frame10():
    global score
    global first_page9
    if entry9.get() =="B":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global entry10
    global frame10
    first_page9 = Toplevel()
    first_page9.geometry("500x500+100+100")
    frame10 = Frame(first_page9)
    frame10.grid(row=0,column=0, sticky='nsew')
    first_page9.title("NBA Question 9")
    lblquestion=Label(frame10,text="""What is the minimum age to be eligible for the NBA draft?
    A. 18
    B. 19
    C. 17""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame10,text="Option:")
    lbloption.grid(row=1,column=0)
    entry10=Entry(frame10)
    entry10.grid(row=1,column=1)
    btn1=Button(frame10,text="Enter",command=frame11)
    btn1.grid(row=2,column=1)
    reset_button9=Button(frame10,text="Reset Quiz",command=lambda: reset_quiz(first_page9))
    reset_button9.grid(row=3,column=1)
    retry_button = Button(frame10, text="Retry Question", command=lambda: retry(first_page8, first_page9))
    retry_button.grid(row=4, column=1)
    skip_button=Button(frame10,text="Skip Question",command=frame11)
    skip_button.grid(row=5,column=1)
    first_page8.withdraw()
#Question 10
def frame11():
    global score
    global first_page10
    first_page10 = Toplevel()
    first_page10.geometry("500x500+100+100")
    if entry10.get() =="B":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global entry11
    global frame11
    frame11 = Frame(first_page10)
    frame11.grid(row=0,column=0, sticky='nsew')
    first_page10.title("NBA Question 10")
    lblquestion=Label(frame11,text="""What is the name of the NBA's All-Star Game MVP award?
    A. Kobe Bryant MVP Award
    B. All- Star Game MVP Award
    C. Best Player Award""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame11,text="Option:")
    lbloption.grid(row=1,column=0)
    entry11=Entry(frame11)
    entry11.grid(row=1,column=1)
    btn1=Button(frame11,text="Enter",command=frame12)
    btn1.grid(row=2,column=1)
    reset_button10=Button(frame11,text="Reset Quiz",command=lambda: reset_quiz(first_page10))
    reset_button10.grid(row=3,column=1)
    retry_button = Button(frame11, text="Retry Question", command=lambda: retry(first_page9, first_page10))
    retry_button.grid(row=4, column=1)
    first_page9.withdraw()
#Score page, last window
def frame12():
    global score
    global page11
    page11 = Toplevel()
    page11.geometry("500x500+100+100")
    global frame12
    if entry11.get() =="A":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    frame12 = Frame(page11   )
    frame12.grid(row=0,column=0, sticky='nsew')
    page11.title("NBA QUIZ SCORE")
    lbl1=Label(frame12,text=f"Well done {entryname.get()}, you scored {score}/10.")
    lbl1.grid(row=0,column=0)
    first_page10.withdraw()                                                     
#Question 1
def first_question():
    #withdraws root, previous window
    root.withdraw()
    global first_page
    #Creates a new page
    first_page = Toplevel()
    first_page.geometry("500x500+100+100")
    first_page.title("NBA Question 1")
    global score
    global entry1
    global frame2
    frame2 = Frame(first_page)
    frame2.grid(row=0,column=0, sticky='nsew')
    lblquestion=Label(frame2,text="""Question:
    What does "NBA" stand for?
    A. National Basketball Account
    B. Nation Basketball Associate
    C. National Basektball Association""")
    lblquestion.grid(row=0,column=0)
    lbloption=Label(frame2,text="Option:")
    lbloption.grid(row=1,column=0)
    entry1=Entry(frame2)
    entry1.grid(row=1,column=1)
    btn1=Button(frame2,text="Enter",command=frame3)
    btn1.grid(row=2,column=1)
    reset_button=Button(frame2,text="Reset Quiz",command=lambda: reset_quiz(first_page))
    reset_button.grid(row=3,column=1)
    skip_button=Button(frame2,text="Skip Question",command=frame3)
    skip_button.grid(row=5,column=1)
def reset_quiz(page):
    page.withdraw()
    import Version_4
    os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
  
def retry(prev_page, page):
    prev_page.deiconify()
    page.withdraw()

    
  
#This is the first window
root=Tk()
root.title("NBA QUIZ")
root.geometry("500x500+100+100")
#score starts from 0
score=0
#Asks for user name
lblname= Label(root, text = "Name :")
lblname.grid(row=0,column=0)

question= Label(root, text= "Are you ready to start")
question.grid(row=1, column=0)

entryname= Entry(root)
entryname.grid(row=0,column=1)
#Button to start the Quiz
btnyes= Button(root,text="yes", command=first_question)   
btnyes.grid(row=1, column=1)

root.mainloop()