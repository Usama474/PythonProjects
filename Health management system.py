#1- Harry 2-Rohan 3-Hammad
def gettime():
    import datetime
    return str(datetime.datetime.now());

def store(a):
    if a==1:
        in4 = int(input("Please tell what do you want to store? \n 1 for food \n 2 for exercise"))
        if in4==1:
            harryfood = input("Please enter the food name")
            with open("harry_food.txt", "a") as f:
                f.write(harryfood);
                f.write(gettime())
        else:
            harryexercise = input("Please enter the exercise name")
            with open("harry_exercise.txt", "a") as f:
                f.write(harryexercise);
                f.write(gettime())
    elif a==2:
        in4 = int(input("Please tell what do you want to store? \n 1 for food \n 2 for exercise"))
        if in4 == 1:
            rohanfood = input("Please enter the food name")
            with open("rohan_food.txt", "a") as f:
                f.write(rohanfood);
                f.write(gettime())
        else:
            rohanexercise = input("Please enter the exercise name")
            with open("rohan_exercise.txt", "a") as f:
                f.write(rohanexercise);
                f.write(gettime())
    else:
        in4 = int(input("Please tell what do you want to store? \n 1 for food \n 2 for exercise"))
        if in4 == 1:
            hammadfood = input("Please enter the food name")
            with open("hammad_food.txt", "a") as f:
                f.write(hammadfood);
                f.write(gettime())
        else:
            hammadexercise = input("Please enter the exercise name")
            with open("hammad_exercise.txt", "a") as f:
                f.write(hammadexercise);
                f.write(gettime())


def retrieve(x):
    if x==1:
        in5 = int(input("Please tell what do you want to read? \n 1 for food \n 2 for exercise"))
        if in5==1:
            with open("harry_food.txt", "r") as f:
                print(f.read());
        else:
            with open("harry_exercise.txt", "r") as f:
                print(f.read());
    elif x==2:
        in5 = int(input("Please tell what do you want to read? \n 1 for food \n 2 for exercise"))
        if in5 == 1:
            with open("rohan_food.txt", "r") as f:
                print(f.read());
        else:
            with open("rohan_exercise.txt", "r") as f:
                print(f.read());
    else:
        in5 = int(input("Please tell what do you want to read? \n 1 for food \n 2 for exercise"))
        if in5 == 1:
            with open("hammad_food.txt", "r") as f:
                print(f.read());
        else:
            with open("hammad_exercise.txt", "r") as f:
                print(f.read());
choice=1

while choice==1:
    in1= int(input("What do you want to do ?\n 1 for store \n 2 For Retrieve"))
    if in1==1:
        in2= int(input("For whome do you want to store ?\n 1 for Harry \n 2 For Rohan \n 3 for Hammad"))
        store(in2);
    else:
        in3 = int(input("For whome do you want to read ?\n 1 for Harry \n 2 For Rohan \n 3 for Hammad"))
        retrieve(in3);
    choice= int(input("Do you want to keep the program running? \n 1 for yes \n 2 for no "))
