secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

chosen_number = int(input("Chosen Number: "))
while chosen_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    chosen_number = int(input("Chosen Number: "))
else:
    print("Well done, muggle! You are free now.")