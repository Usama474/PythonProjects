num= 60
i= 0
while(i<5):
    i+=1;
    in1= int(input("Please enter the number between 1 to 100 to guess"))
    if in1 > num:
        print("The given number is greater than the number. Enter a smaller number! \n You have attempts left", 5-i)
    elif in1< num:
        print("The given number is smaller than the number. Enter a bigger number!  \n You have attempts left", 5-i)

    else:
        print("You have guessed the right number. Congratulations!!!  \n You have done in attempts", i)
        break
