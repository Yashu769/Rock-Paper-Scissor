import random

dict = {'R':"Rock",'P':"Paper",'S':"Scissors"}
user_count = 0
comp_count = 0

games =int(input("Enter the number of games you want to play: ")) 

while(user_count + comp_count < games) :

    flag = 0

    user_input = input("\nUser's Input: ")[0]
    # The [0] after input() will assign the first character of input to the variable(i.e user_input)
    user_input = user_input.upper()

    for i in dict.keys():
        if i == user_input :
            flag = 1
            break 
    if(flag!=1):
        print("Invalid Input")
        continue

    comp_input = random.choice(list(dict.keys()))

    print("Computer's Input: ",dict[comp_input])
    if (user_input == "R" and comp_input == "P") or (user_input == "P" and comp_input == "S") or (user_input == "S" and comp_input == "R"):
        comp_count+=1
    elif (user_input == "P" and comp_input == "R") or (user_input == "S" and comp_input == "P") or (user_input == "R" and comp_input == "S") :
        user_count+=1
    else:
        print("TIE")


    print("\nScore: ")
    print("User Score: ",user_count,"\tComputer Score:",comp_count,"\n") 


print("\n\t\tFINAL SCORE:")
print("User Score: ",user_count,"\t\t\tComputer Score:",comp_count,"\n") 


if user_count<comp_count:
    print("\n\t\tSORRY! YOU LOST !")   
elif user_count>comp_count:
    print("\n\tCONGRATULATIONS! YOU WON!")
else:
    print("\n\t\tOOPS! IT'S A TIE!")




