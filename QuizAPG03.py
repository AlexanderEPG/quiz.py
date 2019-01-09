#1 question and 4 option quiz
#by APG
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
(3)
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

print("you have", score,"point(s)")
