#Create a new text file (in code) called students.txt
#Add lines to it (either manually or in code) for each member of the class
#Loop through the lines and output each one
#Print out the second letter in everyone's name
#Print out every name that is over 6 letters long
#Get the user to add a new name to the file
# type: ignore
 
#!!!!!!!!!CHANGE YOUR FILE NAME TO STUDENTS.TXT OR THE CODE WILL NOT WORK!!!!!!!!!!!!!!!!!!
 
with open("students.txt", "r") as students:
    for line in students:
        print(line.strip())
 
with open("students.txt", "r") as students:
    for line in students:
        print(line[2])
 
with open("students.txt", "r") as students:
    for line in students:
        if len(line) > 6:
            print(line.strip())
 
userinp = input("Insert your own name into file: ")
 
with open("students.txt", "a") as students:
    students.write(userinp + "\n")
    print("Done")