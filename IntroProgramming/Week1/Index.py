"""
I used to be a Programming substitue teacher, I know about programming and I used to use python, it was my first language
I just moved to JavaScript because I like it a little bit more.

In this code you will see a While loop that will ask you for your name, but if you provide something different to a real
name like numbers it will regret you and repeat the question

If you use your name normally you will see it just will continue, but if you try to make a joke, it will ask for your real
name.

Try to use a name like 2323231  or Better4u and you will realise.

In programming this is called data validation.

Thanks you!

"""

while True:
    firstName = input("What is your first name?: ")

    if firstName.isalpha():
        break
    else:
        print(
            "That is an strange name, are you sure about that? please use your real name."
        )

while True:
    lastName = input("What is your last name?: ")

    if lastName.isalpha():
        break
    else:
        print(
            "That is an strange lastname, are you sure about that? please use your real name."
        )


firstName = firstName.capitalize()
lastName = lastName.capitalize()

output = f"Your name is {firstName}, {firstName} is a great name."


response_1 = input(
    f"My name is Jerry, a pleasure {firstName}.  What do you like to do?: "
)

response2 = input(
    f"That's great to know!, I like to check my code and check the binaries, you know ceros and ones,  0001010101 0101010000010111011 and more, is it a little bit boring sometimes but... I can understand their meaning."
)

response_3 = input(f"Te gusta estar en BYU {firstName}?")
