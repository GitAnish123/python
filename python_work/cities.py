# Lets do "while" loops but ending with a "break" statement.
# For example,

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# That is how you do it.






# ----------- PRACTICE -------------- #
""" Practice now begins """


pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

message = ""
while message != "quit":
    message = input(pizza_prompt)
    
    if message != "quit":
        print(f"We are adding {message}")


# 2nd example
movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
while True:
    themovie = input(movie_tickets)
    if themovie == "finished":
        break
    else:
        themovie = int(themovie)
        if themovie <= 3:
            print("It is free to enter.")
        elif themovie <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")

# While conditioning examples
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

message = ""
while message != "quit":
    message = input(pizza_prompt)
    
    if message != "quit":
        print(f"We are adding {message}")


movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
message = ""
while message != "finished":
    message = input(movie_tickets)
    
    if message != "finished":
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")


# Flag examples
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

active = True
while active:
    message = input(pizza_prompt)
    if message == "quit":
        active = False
    else:
        print(f"We are adding {message}")

movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
active = True
while active:
    message = input(movie_tickets)
    if message == "finished":
        active = False
    else:
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")
        



# while "True" with a break value.
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "
while True:
    message = input(pizza_prompt)
    if message == "quit":
        break
    else:
        print(f"We are adding {message}")

movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
while True:
    message = input(movie_tickets)
    if message == "finished":
        break
    else:
        message = int(themovie)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")


# Here is a infinite loop!!!
while 1 == 1:
    print(True)



# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """