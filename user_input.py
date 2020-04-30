# message = input("Tell me something and I'll repeat it back to you:")
# print(message)

#################################

# name = input("Tell me your name and I'll repeat it: ")
# print(f"\nHello, {name}")

#################################

# age = input("How old are you?")
# age = int(age)
# if age <= 21:
#     print(f"I'm sorry, but {age} isn't old enough to enter.")
# else:
#     print(f"Alright, {age} is old enough. Come on in!")

#################################

# number = input("Enter a number and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"The number {number} is odd.")

#################################

# current_num = 10
# while current_num >= 0:
#     print(current_num)
#     current_num -= 1

#################################

# prompt = "\nTell me something and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""

# # while message != 'quit':
# #     message = input(prompt)
    
# #     if message != 'quit':
# #         print(message)
        
# active = True 

# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

#################################

# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)
    
#     if city == 'quit':
#         break
#     else:
#         print(f"\nI'd love to go to {city.title()}!")

#################################

# current_num = 0

# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
    
#     print(current_num)

#################################

# unconfirmed_users = ['Molly', 'Jo', 'Ariel']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
    
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
    
# print("\nThe following users have been confirmed: ")
    
# for confirmed_users in confirmed_users:
#     print(confirmed_users.title())

#################################

# pets = ['dog', 'cat', 'lizard', 'snake', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
    
# print(pets)

#################################

# responses ={}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("\nWhich mountain would you like to climb one day? ")
    
#     responses[name] = response
    
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
        
# print("\n--- Poll Results ---")

# for name, response in responses.items():
#     print(f"\n{name} would like to climb {response}.")