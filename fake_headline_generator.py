# 1- import the random module
import random

# 2- create a list of subjects, verbs, and objects
subjects = ["Shahrukh Khan", 
            "Virat Kohli",
            "Nirmala Sitharaman",
            "A Mumbai Cat",
            "A Group of Monkeys",
            "Prime Minister Modi",
            "Auto Rickshaw Driver from Delhi"
            ]
verbs = ["launches",
         "wins",
         "criticizes",
         "dances with",
         "eats",
         "meets with",
         "announces",
         "dances with",
         "cancels"
         ]
objects = ["at Red Fort",
           "in Mumbai Local Train",
           "during Diwali Festival",
           "with Bollywood Stars",
           "in Parliament",
           "at a Street Food Stall",
           "with a Street Dog",
           "in a Cricket Stadium",
           "at a Political Rally"]

# 3- start the headline generation loop
while True:
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)

    headline = f" BREAKING NEWS: {subject} {verb} {object}!"    
    print("\n" + headline)

    user_input = input("\nDo you want anothe headline? (yes/no):").strip().lower()
    if user_input == "no":
        break

#print goodbye message
print("\nThank you for using the Fake Headline Generator! Goodbye!  ")  