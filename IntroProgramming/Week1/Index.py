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


firstName = firstName.title()
lastName = lastName.title()


output = f"Your name is {lastName}, {firstName} {lastName}."
print(output)
