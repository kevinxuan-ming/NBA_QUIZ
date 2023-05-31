#Allows us to use tkinter widgets
from tkinter import *
from tkinter import ttk    
import os
import sys
#Question 2
def frame3():
    global score
    global first_page2
    #if answers correct adds 1 to the varible 'score'
    if r3_var.get() == 3:  # Check if r3 is selected
        print("Correct!")
        score=score+1 # Add a point to the score

    else:
        print("Wrong Answer")
    global frame3
    global r5_var
    first_page2 = Toplevel()
    first_page2.geometry("655x695+100+100")
    first_page2.title("NBA Question 2")
    first_page2.config(background='orange')
    frame3 = Frame(first_page2, bg='orange')
    frame3.grid(row=0,column=0, sticky='nsew')
    lblquestion=Label(frame3,text="""How many players on the court
      for each team during an NBA game?
   """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r5_var=IntVar()
    r4=Radiobutton(frame3,text="6",value=1, variable= r5_var,background='orange',font=100,fg='red')
    r4.grid(row=1,column=0)
    r5=Radiobutton(frame3,text="5",value=2,variable=r5_var,background='orange',font=100,fg='red')
    r5.grid(row=2,column=0)
    r6=Radiobutton(frame3,text="10",value=3,variable= r5_var,background='orange',font=100,fg='red')
    r6.grid(row=3,column=0)
    btn1=Button(frame3,text="Enter",command=frame4,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button2=Button(frame3,text="Reset Quiz",command=lambda: reset_quiz(first_page2),background='orange',font=100,fg='white', bg="blue")
    reset_button2.grid(row=5,column=0)
    retry_button = Button(frame3, text="Retry Question", command=lambda: retry(first_page, first_page2),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame3,text="Skip Question",command=frame4,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q2_img
    q2_img=ttk.Label(frame3, image=png2, background='orange') 
    q2_img.grid(row=9,column=0) 
    first_page.withdraw()
    labelscore2=Label(frame3,text=f'{score}/10',bg='yellow')
    labelscore2.grid(row=8,column=0)
#Question 3
def frame4():
    global first_page3
    global score
    if r5_var.get() ==2:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame4
    global r8_var
    global first_page3 
    first_page3 = Toplevel()
    first_page3.geometry("655x695+100+100")
    first_page3.config(background='orange')
    frame4 = Frame(first_page3, bg='orange')
    frame4.grid(row=0,column=0, sticky='nsew')
    first_page3.title("NBA Question 3")
    lblquestion=Label(frame4,text="""How many quarters are
    there in an NBA game?
   """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r8_var=IntVar()
    r7=Radiobutton(frame4,text="3",value=1, variable= r8_var,background='orange',font=100,fg='red')
    r7.grid(row=1,column=0)
    r8=Radiobutton(frame4,text="4",value=2,variable=r8_var,background='orange',font=100,fg='red')
    r8.grid(row=2,column=0)
    r9=Radiobutton(frame4,text="2",value=3,variable= r8_var,background='orange',font=100,fg='red')
    r9.grid(row=3,column=0)
    btn1=Button(frame4,text="Enter",command=frame5,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button3=Button(frame4,text="Reset Quiz",command=lambda: reset_quiz(first_page3),background='orange',font=100,fg='white', bg="blue")
    reset_button3.grid(row=5,column=0)
    retry_button = Button(frame4, text="Retry Question", command=lambda: retry(first_page2, first_page3),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame4,text="Skip Question",command=frame5,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q3_img
    q3_img=ttk.Label(frame4, image=png3, background='orange') 
    q3_img.grid(row=9,column=0) 
    first_page2.withdraw()
    #Shows current score
    labelscore3=Label(frame4,text=f'{score}/10',bg='yellow')
    labelscore3.grid(row=8,column=0)
#Question 4
def frame5():
    global first_page4
    global score
    if r8_var.get() ==2:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame5
    global r10_var
    first_page4 = Toplevel()
    first_page4.geometry("655x695+100+100")
    first_page4.config(background='orange')
    frame5 = Frame(first_page4, bg='orange')
    frame5.grid(row=0,column=0, sticky='nsew')
    first_page4.title("NBA Question 4")
    lblquestion=Label(frame5,text="""How many points is a
    three pointer worth?
   """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r10_var=IntVar()
    r10=Radiobutton(frame5,text="3",value=1, variable= r10_var,background='orange',font=100,fg='red')
    r10.grid(row=1,column=0)
    r11=Radiobutton(frame5,text="2",value=2,variable=r10_var,background='orange',font=100,fg='red')
    r11.grid(row=2,column=0)
    r12=Radiobutton(frame5,text="3.5",value=3,variable= r10_var,background='orange',font=100,fg='red')
    r12.grid(row=3,column=0)
    btn1=Button(frame5,text="Enter",command=frame6,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button4=Button(frame5,text="Reset Quiz",command=lambda: reset_quiz(first_page4),background='orange',font=100,fg='white', bg="blue")
    reset_button4.grid(row=5,column=0)
    retry_button = Button(frame5, text="Retry Question", command=lambda: retry(first_page3, first_page4),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame5,text="Skip Question",command=frame6,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q4_img
    q4_img=ttk.Label(frame5, image=png5, background='orange') 
    q4_img.grid(row=9,column=0) 
    first_page3.withdraw()
    #Shows current score
    labelscore3=Label(frame5,text=f'{score}/10',bg='yellow')
    labelscore3.grid(row=8,column=0)
#Question 5
def frame6():
    global score
    global first_page5

    if r10_var.get() ==1:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame6
    global r15_var
    first_page5 = Toplevel()
    first_page5.geometry("655x695+100+100")
    first_page5.config(background='orange')
    frame6 = Frame(first_page5, bg='orange')
    frame6.grid(row=0,column=0, sticky='nsew')
    first_page5.title("NBA Question 5")
    lblquestion=Label(frame6,text="""What is the name of the NBA's 
    3-point shooting contest held during All-Star Weekend?
    """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r15_var=IntVar()
    r13=Radiobutton(frame6,text="Sniper All-Star",value=1, variable= r15_var,background='orange',font=100,fg='red')
    r13.grid(row=1,column=0)
    r14=Radiobutton(frame6,text="Best Shooter",value=2,variable=r15_var,background='orange',font=100,fg='red')
    r14.grid(row=2,column=0)
    r15=Radiobutton(frame6,text="Three-Point Contest",value=3,variable= r15_var,background='orange',font=100,fg='red')
    r15.grid(row=3,column=0)
    btn1=Button(frame6,text="Enter",command=frame7,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button5=Button(frame6,text="Reset Quiz",command=lambda: reset_quiz(first_page5),background='orange',font=100,fg='white', bg="blue")
    reset_button5.grid(row=5,column=0)
    retry_button = Button(frame6, text="Retry Question", command=lambda: retry(first_page4, first_page5),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame6,text="Skip Question",command=frame7,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q5_img
    q5_img=ttk.Label(frame6, image=png4, background='orange') 
    q5_img.grid(row=9,column=0) 
    first_page4.withdraw()
    #Shows current score
    labelscore4=Label(frame6,text=f'{score}/10',bg='yellow')
    labelscore4.grid(row=8,column=0)
#Question 6   
def frame7():
    global score
    global first_page6
    if r15_var.get() ==3:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global frame7
    global r16_var
    first_page6 = Toplevel()
    first_page6.geometry("655x695+100+100")
    first_page6.config(background='orange')
    frame7 = Frame(first_page6, bg='orange')
    frame7.grid(row=0,column=0, sticky='nsew')
    first_page6.title("NBA Question 6")
    lblquestion=Label(frame7,text="""What is the name of the 
    championship trophy?
    """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r16_var=IntVar()
    r16=Radiobutton(frame7,text="Larry O'Brien NBA Championship Trophy",value=1, variable= r16_var,background='orange',font=100,fg='red')
    r16.grid(row=1,column=0)
    r17=Radiobutton(frame7,text="Season NBA Championship Trophy",value=2,variable=r16_var,background='orange',font=100,fg='red')
    r17.grid(row=2,column=0)
    r18=Radiobutton(frame7,text="Michael Jordan NBA Championship Trophy",value=3,variable= r16_var,background='orange',font=100,fg='red')
    r18.grid(row=3,column=0)
    btn1=Button(frame7,text="Enter",command=frame8,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button6=Button(frame7,text="Reset Quiz",command=lambda: reset_quiz(first_page6),background='orange',font=100,fg='white', bg="blue")
    reset_button6.grid(row=5,column=0)
    retry_button = Button(frame7, text="Retry Question", command=lambda: retry(first_page5, first_page6),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame7,text="Skip Question",command=frame8,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q6_img
    q6_img=ttk.Label(frame7, image=png6, background='orange') 
    q6_img.grid(row=9,column=0) 
    first_page5.withdraw()
    #Shows current score
    labelscore5=Label(frame7,text=f'{score}/10',bg='yellow')
    labelscore5.grid(row=8,column=0)
#Question 7  
def frame8():
    global score
    global first_page7
    if r16_var.get() ==1: 
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global r21_var
    global frame8
    first_page7 = Toplevel()
    first_page7.geometry("655x695+100+100")
    first_page7.config(background='orange')

    frame8 = Frame(first_page7, bg='orange')
    frame8.grid(row=0,column=0, sticky='nsew')
    first_page7.title("NBA Question 7")
    lblquestion=Label(frame8,text="""Who is the NBA's logo modeled after?
    """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r21_var=IntVar()
    r19=Radiobutton(frame8,text="Michael Jordan",value=1, variable= r21_var,background='orange',font=100,fg='red')
    r19.grid(row=1,column=0)
    r20=Radiobutton(frame8,text="Magic Johnson",value=2,variable=r21_var,background='orange',font=100,fg='red')
    r20.grid(row=2,column=0)
    r21=Radiobutton(frame8,text="Jerry West",value=3,variable= r21_var,background='orange',font=100,fg='red')
    r21.grid(row=3,column=0)
    btn1=Button(frame8,text="Enter",command=frame9,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button7=Button(frame8,text="Reset Quiz",command=lambda: reset_quiz(first_page7),background='orange',font=100,fg='white', bg="blue")
    reset_button7.grid(row=5,column=0)
    retry_button = Button(frame8, text="Retry Question", command=lambda: retry(first_page6, first_page7),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame8,text="Skip Question",command=frame9,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q7_img
    q7_img=ttk.Label(frame8, image=png7, background='orange') 
    q7_img.grid(row=9,column=0) 
    first_page6.withdraw()
    #Shows current score
    labelscore6=Label(frame8,text=f'{score}/10',bg='yellow')
    labelscore6.grid(row=8,column=0)
#Question 8 
def frame9():
    global score
    global first_page8
    if r21_var.get() ==3:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global r23_var
    global frame9
    first_page8 = Toplevel()
    first_page8.geometry("655x695+100+100")
    first_page8.config(background='orange')
    frame9 = Frame(first_page8, bg='orange')
    frame9.grid(row=0,column=0, sticky='nsew')
    first_page8.title("NBA Question 8")
    lblquestion=Label(frame9,text="""How long is an NBA regulation game?
    """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r23_var=IntVar()
    r22=Radiobutton(frame9,text="60 minutes",value=1, variable= r23_var,background='orange',font=100,fg='red')
    r22.grid(row=1,column=0)
    r23=Radiobutton(frame9,text="48 minutes",value=2,variable=r23_var,background='orange',font=100,fg='red')
    r23.grid(row=2,column=0)
    r24=Radiobutton(frame9,text="52 minutes",value=3,variable= r23_var,background='orange',font=100,fg='red')
    r24.grid(row=3,column=0)
    btn1=Button(frame9,text="Enter",command=frame10,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button8=Button(frame9,text="Reset Quiz",command=lambda: reset_quiz(first_page8),background='orange',font=100,fg='white', bg="blue")
    reset_button8.grid(row=5,column=0)
    retry_button = Button(frame9, text="Retry Question", command=lambda: retry(first_page7, first_page8),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame9,text="Skip Question",command=frame10,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q8_img
    q8_img=ttk.Label(frame9, image=png8, background='orange') 
    q8_img.grid(row=9,column=0) 
    first_page7.withdraw()
    #Shows current score
    labelscore7=Label(frame9,text=f'{score}/10',bg='yellow')
    labelscore7.grid(row=8,column=0)
#Question 9
def frame10():
    global score
    global first_page9
    if r23_var.get() ==2  :
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global r26_var
    global frame10
    first_page9 = Toplevel()
    first_page9.geometry("655x695+100+100")
    first_page9.config(background='orange')
    frame10 = Frame(first_page9, bg='orange')
    frame10.grid(row=0,column=0, sticky='nsew')
    first_page9.title("NBA Question 9")
    lblquestion=Label(frame10,text="""What is the minimum age to be eligible for the NBA draft?
    """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r26_var=IntVar()
    r25=Radiobutton(frame10,text="18",value=1, variable= r26_var,background='orange',font=100,fg='red')
    r25.grid(row=1,column=0)
    r26=Radiobutton(frame10,text="19",value=2,variable=r26_var,background='orange',font=100,fg='red')
    r26.grid(row=2,column=0)
    r27=Radiobutton(frame10,text="17",value=3,variable= r26_var,background='orange',font=100,fg='red')
    r27.grid(row=3,column=0)
    btn1=Button(frame10,text="Enter",command=frame11,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button9=Button(frame10,text="Reset Quiz",command=lambda: reset_quiz(first_page9),background='orange',font=100,fg='white', bg="blue")
    reset_button9.grid(row=5,column=0)
    retry_button = Button(frame10, text="Retry Question", command=lambda: retry(first_page8, first_page9),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame10,text="Skip Question",command=frame11,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)
    #Call Photo
    global q9_img
    q9_img=ttk.Label(frame10, image=png9, background='orange') 
    q9_img.grid(row=9,column=0) 
    first_page8.withdraw()
    #Shows current score
    labelscore8=Label(frame10,text=f'{score}/10',bg='yellow')
    labelscore8.grid(row=8,column=0)
#Question 10
def frame11():
    global score
    global first_page10
    first_page10 = Toplevel()
    first_page10.geometry("655x695+100+100")
    if r26_var.get() ==2:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    global r28_var
    global frame11
    frame11 = Frame(first_page10, bg='orange')
    frame11.grid(row=0,column=0, sticky='nsew')
    first_page10.config(background='orange')  
    first_page10.title("NBA Question 10")
    lblquestion=Label(frame11,text="""What is the name of the NBA's All-Star Game MVP award?
""",background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r28_var=IntVar()
    r28=Radiobutton(frame11,text="Kobe Bryant MVP Award",value=1, variable= r28_var,background='orange',font=100,fg='red')
    r28.grid(row=1,column=0)
    r29=Radiobutton(frame11,text="All- Star Game MVP Award",value=2,variable=r28_var,background='orange',font=100,fg='red')
    r29.grid(row=2,column=0)
    r30=Radiobutton(frame11,text="Best Player Award",value=3,variable= r28_var,background='orange',font=100,fg='red')
    r30.grid(row=3,column=0)
    btn1=Button(frame11,text="Enter",command=frame12,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button10=Button(frame11,text="Reset Quiz",command=lambda: reset_quiz(first_page10),background='orange',font=100,fg='white', bg="blue")
    reset_button10.grid(row=5,column=0)
    retry_button = Button(frame11, text="Retry Question", command=lambda: retry(first_page9, first_page10),background='orange',font=100,fg='white', bg="blue")
    retry_button.grid(row=6, column=0)
    skip_button=Button(frame11,text="Skip Question",command=frame12,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=7,column=0)  
    #Call Photo
    global q10_img
    q10_img=ttk.Label(frame11, image=png10, background='orange') 
    q10_img.grid(row=9,column=0) 
    first_page9.withdraw()
    #Shows current score
    labelscore9=Label(frame11,text=f'{score}/10',bg='yellow')
    labelscore9.grid(row=8,column=0)
#Score page, last window
def frame12():
    global score
    global page11
    page11 = Toplevel()
    page11.geometry("655x695+100+100")
    page11.config(background='orange')
    global frame12
    if r28_var.get() ==1:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong Answer")
    frame12 = Frame(page11, bg='orange')
    frame12.grid(row=0,column=0, sticky='nsew')
    page11.title("NBA QUIZ SCORE")
    lbl1=Label(frame12,text=f"""Well done {entryname.get()}, you have came to an end to the quiz 
    would you like to:""",font=100,fg='white',bg="orange")
    #options for the combo box  
    options= ["View Score","Retry Quiz","Exit"]
    combo=ttk.Combobox(frame12, values=options,background='orange')
    combo.grid(row=1,column=0)
    lbl1.grid(row=0,column=0)
    def handleSelection(event):
        if combo.get()=="View Score":
            # Command print_score()
            print_score()
        elif combo.get()=="Retry Quiz":
            #Command reset_quiz()
            reset_quiz(page11)
        elif combo.get()=="Exit":
            #command quit_quiz
            quit_quiz()
    combo.bind("<<ComboboxSelected>>", handleSelection)
    global end_img
    end_img=ttk.Label(frame2, image=png11, background='orange') 
    end_img.grid(row=2,column=0) 
    #Call Photo
    global q11_img
    q11_img=ttk.Label(frame12, image=png11, background='orange') 
    q11_img.grid(row=8,column=0) 
    first_page10.withdraw()

def print_score():
    score0=Label(frame12,text=f"Well done {entryname.get()}, you scored {score}/10.",bg='green',fg='white')
    score0.grid(row=2,column=0)

def quit_quiz():
    #destroy page 11, thus exit program
    page11.destroy()

#Question 1
def first_question():
    #withdraws root, previous window
    root.withdraw()
    global first_page
    #Creates a new page
    first_page = Toplevel()
    first_page.geometry("655x695+100+100")
    first_page.title("NBA Question 1")
    global score
    global r3_var
    global frame2
    first_page.config(background='orange')
    frame2 = Frame(first_page, bg='orange')
    frame2.grid(row=0,column=0, sticky='nsew')
    lblquestion=Label(frame2,text="""Question:
    What does "NBA" stand for?
   """,background='orange',font=100,fg='white')
    lblquestion.grid(row=0,column=0)
    r3_var=IntVar()
    r1=Radiobutton(frame2,text="National Basketball Account",value=1, variable= r3_var,background='orange',font=100,fg='red')
    r1.grid(row=1,column=0)
    r2=Radiobutton(frame2,text="Nation Basketball Associate",value=2,variable=r3_var,background='orange',font=100,fg='red')
    r2.grid(row=2,column=0)
    r3=Radiobutton(frame2,text="National Basketball Association",value=3,variable= r3_var,background='orange',font=100,fg='red')
    r3.grid(row=3,column=0)
    btn1=Button(frame2,text="Enter",command=frame3,background='orange',font=100,fg='white', bg="green")
    btn1.grid(row=4,column=0)
    reset_button=Button(frame2,text="Reset Quiz",command=lambda: reset_quiz(first_page),background='orange',font=100,fg='white', bg="blue")
    reset_button.grid(row=5,column=0)
    skip_button=Button(frame2,text="Skip Question",command=frame3,background='orange',font=100,fg='white', bg="blue")
    skip_button.grid(row=6,column=0)
    #Show current score
    labelscore=Label(frame2,text=f'{score}/10',bg='yellow')
    labelscore.grid(row=7,column=0)
    #Calling photo
    global q1_img
    q1_img=ttk.Label(frame2, image=png1, background='orange') 
    q1_img.grid(row=8,column=0) 
def reset_quiz(page):
    page.withdraw()
    import Version_5
    os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
def retry(prev_page, page):
    prev_page.deiconify()
    page.withdraw()
#This is the first window
root=Toplevel()
root.title("NBA QUIZ")
root.geometry("1000x500+100+100")
root.config(bg='orange')
#Importing image
png1=PhotoImage(file='q1.png')
png2=PhotoImage(file='q2.png')
png3=PhotoImage(file='q3.png')
png4=PhotoImage(file='q4.png')
png5=PhotoImage(file='q5.png')
png6=PhotoImage(file='q6.png')
png7=PhotoImage(file='q7.png')
png8=PhotoImage(file='q8.png')
png9=PhotoImage(file='q9.png')
png10=PhotoImage(file='q10.png')
png11=PhotoImage(file='well_done.png.png')
nba=PhotoImage(file='NBA_logo.png')
label=ttk.Label(root, image=nba, background='orange')
label.grid(row=2,column=0)
#score starts from 0
score=0
#Asks for user name
lblname= Label(root, text = "Name :",background='orange',font=100,fg='white')
lblname.grid(row=0,column=0)

question= Label(root, text= "Are you ready to start",background='orange',font=100,fg='white')
question.grid(row=1, column=0)
   
entryname= Entry(root,font=100)
entryname.grid(row=0,column=1)
#Button to start the Quiz
btnyes= Button(root,text="yes", command=first_question,font=100,fg='white', bg="red")   
btnyes.grid(row=1, column=1)

root.attributes('-topmost', 'true')

root.mainloop()