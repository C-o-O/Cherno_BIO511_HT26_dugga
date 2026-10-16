import sys, matplotlib.pyplot as plt, seaborn as sns, pandas as pd, random

my_name = "Cherno" #Creating the string variable my_name, equaling the string "Cherno"

print(len(my_name))  #Prints the length of the my_name string variable

times_of_e = 0  #Variable to count the number of times the letter 'e' occurs in my name. Starts at 0.

for i in my_name:   #For loop through the my_name variable.
    if i == "e":            #If the iteration of i through the my_name variable matches the character 'e'...
        times_of_e += 1     #...add 1 count to the times_of_e variable

print(times_of_e)           #Prints the number of times the 'e' character occurs.

my_list = [1, 5, "4", "six", 3.14] #Creating list my_list
print(my_list)
new_list = []                      #Creating empty list new_list

for item in my_list:                                 #Looping through my_list
    if item in my_list != type(int):                 #If iteration item through my_list is NOT of type int,
        try:                                                       
            new_list.append(int(item))               #Will "try" to convert item to an int and append that it to new_list
        except ValueError:                           #Exception handling where if ValueError is found, i.e. 'item' is of a type that can not be converted to an int...
            print(f"Skipping invalid value: {item}") #...a meaningful message is printed

print(new_list)                                      #Prints the new_list of items that were successfully converted to int


def clean_list(listing):

    new_list = []

    for item in my_list:                                 #Looping through my_list
        if item in my_list != type(int):                 #If iteration item through my_list is NOT of type int,
            try:                                                       
                new_list.append(int(item))                                              #Will "try" to convert item to an int and append that it to new_list
            except ValueError:                                                          #Exception handling where if ValueError is found, i.e. 'item' is of a type that can not be converted to an int...
                print(f"clean_list() called - Skipping invalid value: {item}")          #...a meaningful message is printed                                    
    
    return new_list                                                                     #"Saving" new list as a return value

test = clean_list(my_list)                                                              #Calling function clean_list with the variable test, using my_list as input

print(f"Printing output of clean_list() function {test}")                               #Prints the test variable. Output should be equivalent of the return value defined in function clean_list()


sum_neighbour = [] #Empty list


for v in new_list:
    sum_neighbour = new_list[v] + new_list[v+1] #Value of one summed with value in next index


print(sum_neighbour) #Prints new list where all neighbours have been summed


#Question 3

input = sys.argv[1] #First argument from command line is the python script - then input csv file as defined here

output = sys.argv[2] #Next argument from the command line is the output file (eg. savefile.png)

dframe = pd.read_csv(input) #Pandas reads csv file into a DataFrame, with data as the .csv file

print(dframe)

sns.scatterplot(
    data=dframe,
    x="position_mb",
    y="log2_ratio",
)

plt.savefig(f'{output}') #Plot is saved with the output file name as defined above

#Question 4

dict = {}

games = 0

print(Bob_roll)

while games < 20 #While number of games is less than 20
    Bob_roll = random.randint(1,6) #Bob rolls a random number
    Alice_roll = random.randint(1,6) #Alice rolls a random number
    
    if Bob_roll > Alice_Roll    #If Bob has a greater dice roll than Alice
        dict                    #Append to dictionary as victory for Bob
    if Bob_roll < Alice_Roll    #If Bob has a lower dice roll than Alice.
        dict                    #Append to dictionary as victory for Alice
    if Bob_roll == Alice_Roll   #If Bob and Alice have equal dice rolls
        dict                    #Append to dictionary as draw
    
    games += 1                  #+1 number of games

print(dict)                     #Print dictionary with game result

def dice(player1,player2,ngames) #Function of dicegame. Same-ish commentary as above
    games = 0
    while games < ngames
    Bob_roll = random.randint(1,6)
    Alice_roll = random.randint(1,6)
    if Bob_roll > Alice_Roll
        dict
    if Bob_roll < Alice_Roll
        dict
    if Bob_roll == Alice_Roll
        dict
    
    games += 1
    return dict

dicegame = dice(me,you,50)

print(dicegame)