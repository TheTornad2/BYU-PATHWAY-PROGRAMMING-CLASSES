""" 
 In this enhanced version, I have added several features to make the meal calculator more engaging and interactive:
 1. A random meal suggestion is provided to help users decide what to eat.
 2. Users can now add drinks and desserts to their order, allowing for a more realistic dining experience.
 3. A playful compliment is given based on the tip percentage, making the interaction more enjoyable.
 These features aim to enhance user experience while fulfilling all project requirements.
"""

import random

# Fun list of meal suggestions
meal_suggestions = [
    "Pizza Party",
    "Taco Fiesta",
    "Burger Bash",
    "Sushi Night",
    "Pasta Paradise",
]

# Meal Price Calculator with Fun Additions
print("Welcome to the Fun Meal Price Calculator!\n")

# Random meal suggestion
random_meal = random.choice(meal_suggestions)
print(f"Feeling indecisive? How about trying our '{random_meal}' special?\n")

# Ask for the price of a child's meal and an adult's meal
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask for the number of children and adults
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Ask if they want drinks and desserts
drink_price = float(
    input("\nWould you like to add drinks? Enter the price per drink: ")
)
dessert_price = float(input("How about desserts? Enter the price per dessert: "))

# Calculate the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Drinks and desserts calculations
num_drinks = int(input("\nHow many drinks would you like to add? "))
num_desserts = int(input("How many desserts would you like to add? "))

drink_total = drink_price * num_drinks
dessert_total = dessert_price * num_desserts

# New subtotal with drinks and desserts
subtotal_with_extras = subtotal + drink_total + dessert_total
print(f"\nSubtotal (Including Drinks & Desserts): ${subtotal_with_extras:.2f}")

# Ask for the sales tax rate
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Calculate and display the sales tax
sales_tax = subtotal_with_extras * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate the total price
total = subtotal_with_extras + sales_tax
print(f"Total: ${total:.2f}")

# Ask for the payment amount
payment = float(input("\nWhat is the payment amount? "))

# Calculate and display the change
change = payment - total
print(f"Change: ${change:.2f}")

# Fun Tip Feature
tip_percentage = float(
    input("\nWould you like to leave a tip? Enter the tip percentage: ")
)
tip = total * (tip_percentage / 100)

# Calculate the final total including the tip
final_total = total + tip

# Compliment based on the tip amount
if tip_percentage >= 20:
    compliment = "Wow, you're generous! You're making someone's day!"
elif tip_percentage >= 10:
    compliment = "Thanks for the tip! You're awesome!"
else:
    compliment = "Every bit helps! You're still great!"

print(f"\nTip: ${tip:.2f}")
print(f"Final Total (including tip): ${final_total:.2f}")
print(compliment)
