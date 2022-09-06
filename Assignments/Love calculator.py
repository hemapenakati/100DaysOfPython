'''You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score.

"Your score is **z**."'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
couple = name1 + name2
total1 = couple.count("t") + couple.count("r") + couple.count("u") + couple.count("e")
total2 = couple.count("l") + couple.count("o") + couple.count("v") + couple.count("e")
total = str(total1) + str(total2)
total = int(total)
if total < 10 or total >90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 < total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
