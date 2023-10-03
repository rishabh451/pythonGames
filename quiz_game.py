print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :)")    
score = 0

    
answer = input("The correct extension of the Python file is? ")
if answer.lower() == ".py":
    print("correct!")
    score += 1 
else:
    print("Incorrect!")  

answer = input("What does pip stand for in python? ")
if answer.lower() == "preferred installer program":
    print("correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("Which keyword is used for function in Python language? ")
if answer.lower() == "def":
    print("correct!")
    score += 1 

else:
    print("Incorrect!") 

answer = input("What is the comment symbol in python? ")
if answer.lower() == "#":
    print("correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("What is the difference between list and tuples in Python? ")
if answer.lower() == "list is mutable and tuple is immutable":
    print("correct!")
    score += 1 
else:
    print("Incorrect!")        

print("You got " + str(score) + " questions correct!")
