"""
This is my calculator, this time i could not get a lot of inspiration, I am a little bit tired from my job, but I hope you enjoy it 😅😅😅😅
"""

print(
    "-------------------------------------WELCOME TO THE GRADE CALCULATOR-------------------------------------"
)

grade = int(input("Please enter your grade: "))


if grade >= 90:
    letter = "A, You are doing it great!"
    if grade >= 97:
        letter = "A+"
    elif grade < 93:
        letter = "A-, Keep pushing!"
elif grade >= 80:
    if grade >= 87:
        letter = "B+, Well done, let's go for more!"
    elif grade >= 83:
        letter = "B-, Good job, keep improving!"
    else:
        letter = "B, Well done, let's go for more!"
elif grade >= 70:
    if grade >= 77:
        letter = "C+, You’re getting there!"
    elif grade >= 73:
        letter = "C-, Keep at it, you can improve!"
    else:
        letter = "C, Not bad at all, but I know we can do it better!"
elif grade >= 60:
    if grade >= 67:
        letter = "D+, We need to grow, let's make an effort to obtain better results!"
    elif grade >= 63:
        letter = "D-, Don't give up, keep trying!"
    else:
        letter = "D, We need to grow, let's make an effort to obtain better results I know you can!\nRemember that we need 70 to pass."
else:
    letter = "F, We need to work harder!"


print(f"Your letter grade is: {letter}")

print(
    "-------------------------------------RESULT-------------------------------------"
)

if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
