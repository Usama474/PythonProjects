#snake water gun
import random
l= ["Snake", "Water", "Gun"]
my_score=0;
com_score=0;
i=0;
while(i<10):
    i+=1;
    in1= input("Please enter your choice from \n s for Snake \n w for Water \n g for Gun");
    x= random.choice(l)
    if in1=="s" and x=="Water":
        print(f"Turn {i}.You chose Snake and computer chose {x}. You won!")
        my_score+=1;
    elif in1=="s" and x=="Gun":
        print(f"Turn {i}.You chose Snake and computer chose {x}. You lost!")
        com_score+=1;
    elif in1=="s" and x=="Snake":
        print(f"Turn {i}.You both chose the same option {x}. Drawn!! ");
    elif in1=="w" and x=="Water":
        print(f"Turn {i}.You both chose the same option {x}. Drawn!! ");
    elif in1 == "w" and x == "Snake":
        print(f"Turn {i}.You chose Water and computer chose {x}. You lost!")
        com_score+=1;
    elif in1 == "w" and x == "Gun":
        print(f"Turn {i}.You chose Water and computer chose {x}. You won!")
        my_score+=1;
    elif in1 == "g" and x == "Gun":
        print(f"Turn {i}.You both chose the same option {x}. Drawn!! ");
    elif in1 == "g" and x == "Water":
        print(f"Turn {i}.You chose Gun and computer chose {x}. You lost!")
        com_score += 1;
    else:
        print(f"Turn {i}.You chose Gun and computer chose {x}. You won!")
        my_score += 1;

print(f"Result \nYou won {my_score} times\nComputer won {com_score} times");



