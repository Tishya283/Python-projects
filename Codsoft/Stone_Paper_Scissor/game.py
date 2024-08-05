import random
your_score=0
computer_score=0
def game():
    global your_score
    global computer_score
    computer = random.choice([1, 0, -1])
    youStr=input("""(for stone enter stone,\n for paper enter paper, \n for scissor enter scissor)\n \nenter your choice:""")
    youDict ={"stone": 1, "paper": -1, "scissor": 0}
    reversedDict ={1:"stone",-1:"paper", 0:"scissor"}

    
    you=youDict[youStr]
    print("\n\n\n")
    print(f"the computer choose:{reversedDict[computer]}")
    print(f"you choose:{reversedDict[you]}")
    
    if(computer == you):
        a=print("draw")
        your_score=your_score
        computer_score=computer_score
    elif(computer==0) and (you==1):
        a=print("you won!")
        your_score+=1
    elif(computer==0) and (you==-1):
        a=print("you lose!")
        computer_score+=1
    elif(computer==1) and (you==0):
        a=print("you lose!")
        computer_score+=1
    elif(computer==1) and (you==-1):
        a=print("you won!")
        your_score+=1
    elif(computer==-1) and (you==1):
        a=print("you lose!")   
        computer_score+=1
    elif(computer==-1) and (you==0):
        a=print("you won!")
        your_score+=1
    else:
        a=print("Something went wrong")
    print(f"your score is:{your_score}")
    print(f"computer's score is:{computer_score}")
    print("\n\n")
    
for i in range(0,5):
    game()


print(f"your final score is:{your_score}")
print(f"computer's final score is:{computer_score}")
if(your_score>computer_score):
    print("you won the game")
elif(your_score<computer_score):
    print("you loss the game")
else:
    print("game draw")