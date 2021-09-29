# author: CCG 9/29/21

grade = input("What is your grade for the quarter?")

if int(grade) < 60:
    print("You got an F")
elif int(grade) < 65:
    print("You got an D")
elif int(grade) < 70:
    print("You got an D+")
elif int(grade) < 73:
    print("You got an C-")
elif int(grade) < 77:
    print("You got an C")
elif int(grade) < 80:
    print("You got an C+")
elif int(grade) < 83:
    print("You got an B-")
elif int(grade) < 87:
    print("You got an B")
elif int(grade) < 90:
    print("You got an B+")
elif int(grade) < 93:
    print("You got an A-")
elif int(grade) < 100:
    print("You got an A")
else:
    print("You got an incorrect percentile average")
