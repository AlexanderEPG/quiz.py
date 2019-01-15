# 10 question 4 option quiz
#by APG

#custom function
def run_quest(quest,check,ansU,ansR):
    while check == False:
        print (quest)
        try:
                ansU = int(input("Your answer >"))
                if ansU == ansR:
                        score += 1
                        check = True
                elif 0 < ansU < 5:
                        check = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")
                
score = int(0)
qA = int()
q1 = False
q2 = False
q3 = False
q4 = False
q5 = False
q6 = False
q7 = False
q8 = False
q9 = False
q10 = False


print("choose from the choices below by choosing the number of the option")
print()
print()


Q1 = print("""what is 1 + 1?
(1)54
(2)2
(3)625
(4)*click*""")

while q1 == False:
        print (Q1)
        try:
                qA = int(input("Your answer >"))
                if qA == 2:
                        score += 1
                        q1 = True
                elif 0 < qA < 4:
                        q1 = True
                elif qA == 4:
                        print("my brotha, do you know da wey")
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q2 = print("""what is the square root of 625?
(1)25
(2)15
(3)65
(4)69""")
while q2 == False:
        print (Q2)
        try:
                qA = int(input("Your answer >"))
                if qA == 1:
                        score += 1
                        q2 = True
                elif 0 < qA < 4:
                        q2 = True
                elif qA == 4:
                        print("hahaha( ͡° ͜ʖ ͡°)")
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q3 = print("""what is pi?
(1)3.1414926....
(2)3.1415326....
(3)1.523632....
(4)3.1415926...""")
while q3 == False:
        print (Q3)
        try:
                qA = int(input("Your answer >"))
                if qA == 4:
                        score += 1
                        q3 = True
                elif 0 < qA < 5:
                        q3 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")

Q4 = print("""how much wood could a woodchuck chuck if a woodchuck could chuck wood
(1)3
(2)700
(3)0
(4)165937""")
while q4 == False:
        print (Q4)
        try:
                qA = int(input("Your answer >"))
                if qA == 3:
                        score += 1
                        q4 = True
                elif 0 < qA < 5:
                        q4 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q5 = print("""what is 9+10?
(1)19
(2)21
(3)1
(4)-20""")
while q5 == False:
        print (Q5)
        try:
                qA = int(input("Your answer >"))
                if qA == 1:
                        score += 1
                        q5 = True
                elif 0 < qA < 5:
                        q5 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q6 = print("""who is the strongest?
(1)Son Goku
(2)Sin of Pride Escanor
(3)you the user
(4)Naruto""")
while q6 == False:
        print (Q6)
        try:
                qA = int(input("Your answer >"))
                if qA == 1:
                        score += 1
                        q6 = True
                elif 0 < qA < 5:
                        q6 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q7 = print("""what is the password if the person said 12345678
(1)12345678
(2)2444666668888888
(3)122333444455555666666777777788888888
(4)11333355555577777777""")
while q7== False:
        print (Q7)
        try:
                qA = int(input("Your answer >"))
                if qA == 2:
                        score += 1
                        q7 = True
                elif 0 < qA < 5:
                        q7 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")

Q8 = print("""
To get in the club you decide to hear what the password is.The security said six,
person 1 replied three, then another person came along and the security said twelve,
person 2 replied six. What is the code to enter if the security said to you ten?

(1)five
(2)two
(3)ten
(4)three""")
while q8 == False:
        print (Q8)
        try:
                qA = int(input("Your answer >"))
                if qA == 4:
                        score += 1
                        q8= True
                elif 0 < qA < 5:
                        q8 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q9 = print("""
You are a special agent trying to get in a suspecious cult, you decide to wait and hear what the password
is, the message box at the door said 6, person 1 responded 3 then the message box procceded to ask person 2
that was right behind person 1 and said 3, person 2 responded 2, you found out that to get in you need a
person, you wait for another person to show up and the message box said 10, person 3 responded 2, the
message box said to you 2, what do you respond with?

(1)five
(2)two
(3)ten
(4)three""")
while q9 == False:
        print (Q9)
        try:
                qA = int(input("Your answer >"))
                if qA == 1:
                        score += 1
                        q9= True
                elif 0 < qA < 5:
                        q9 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q10 = print("""what is 10^10

(1)10000000000
(2)100000000000
(3)1
(4)5""")

while q10 == False:
        print (Q10)
        try:
                qA = int(input("Your answer >"))
                if qA == 1:
                        score += 1
                        q10 = True
                elif 0 < qA < 5:
                        q10 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")

print("you have", score,"/10 correct")
