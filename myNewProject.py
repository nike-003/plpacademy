score=0
print("1.What is the output of 2+2 ?")
print("a)3")
print("b)4")
print("c)5")
answer1=input("your answer:")
if answer1.lower()=="b":
    print("correct")
score+=1
print("Wrong! The correct answer is b)4")
print()
print("2.Which language is this quiz written in ?")
print("a)java")
print("b)c++")
print("c)python")
answer2=input("your answer:")
if answer2.lower()=="c":
     print("correct")
score+=1
print("Wrong!The correct answer is C)python")
print()
print(f"you got {score} out of 2")