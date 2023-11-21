# Lets learn to modify functions!
# Learn more in notes or in crash course!
# Here is an example without functions with 3D Models!




# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)





# Here is an example with 2 functions with each doing a specific job
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)   # This list will be empty due to the modifyment.
# That is an example of how it will work. This is way effietient and much easier to work with!



# You can also send a copy to a function so when you modify it, the function will not change its elements inside.
# This will work for "unprinted_designs" in the function, "print_models" in this example. For example:

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs) # This list will not be empty because we made a copy and will be the same as the completed models.
# That is an example of how you do it!





# ----------- PRACTICE -------------- #
""" Practice now begins """



# Passing a list simple example
def show_messages(short_text_messages):
    """Print short text messages that are shown in a list."""
    for message in short_text_messages:
        print(f"Short Text Message: {message}, ")

list_of_14_common_messages = ['BRB', 'LOL', 'OMG', 'BTW', 'IDK', 'GM', 'WSG', 'GN', 'OMW', 'OML', 'OFC', 'SMH', 'NBD', 'OM']
show_messages(list_of_14_common_messages)





# Modifying a list along with passing it example
def show_messages(short_text_messages):
    """Print short text messages that are shown in a list."""
    print("Showing all the messages:")
    for message in short_text_messages:
        print(f"Short Text Message: {message}, ")


def send_messages(sending_messages, sent_messages):
    """Make sure the messages that are about to send in a list are sent and moved to another list."""
    print("Sending all messages.")
    while sending_messages:
        messaged = sending_messages.pop()
        print(f"Sending message: {messaged}")
        sent_messages.append(messaged)

list_of_14_common_messages = ['BRB', 'LOL', 'OMG', 'BTW', 'IDK', 'GM', 'WSG', 'GN', 'OMW', 'OML', 'OFC', 'SMH', 'NBD', 'OM']
requested_messages_to_send = []
show_messages(list_of_14_common_messages)
send_messages(list_of_14_common_messages, requested_messages_to_send)

print("\nFinal lists: ")
print(list_of_14_common_messages) # This list should be empty
print(requested_messages_to_send) # This list should be full with messages




# Extended program with two functions:
def show_messages(short_text_messages):
    """Print short text messages that are shown in a list."""
    print("Showing all the messages:")
    for message in short_text_messages:
        print(f"Short Text Message: {message}, ")


def send_messages(sending_messages, sent_messages):
    """Make sure the messages that are about to send in a list are sent and moved to another list."""
    print("Sending all messages.")
    while sending_messages:
        messaged = sending_messages.pop()
        print(f"Sending message: {messaged}")
        sent_messages.append(messaged)

def display_messages(sent_messages):
    """Display all the messages that are moved into the final list of the sent messages. The result must be in a list."""
    print("\nDisplaying all the messages: ")
    for messag in sent_messages:
        print(messag)

list_of_14_common_messages = ['BRB', 'LOL', 'OMG', 'BTW', 'IDK', 'GM', 'WSG', 'GN', 'OMW', 'OML', 'OFC', 'SMH', 'NBD', 'OM']
requested_messages_to_send = []
show_messages(list_of_14_common_messages)
send_messages(list_of_14_common_messages, requested_messages_to_send)
display_messages(requested_messages_to_send)

print("\nFinal lists: ")
print(list_of_14_common_messages) # This list should be empty
print(requested_messages_to_send) # This list should be full with messages



# Preventing a list from modifying by making a copy of the starting list. We are doing the non-extended version
def show_messages(short_text_messages):
    """Print short text messages that are shown in a list."""
    print("Showing all the messages:")
    for message in short_text_messages:
        print(f"Short Text Message: {message}, ")


def send_messages(sending_messages, sent_messages):
    """Make sure the messages that are about to send in a list are sent and moved to another list."""
    print("Sending all messages.")
    while sending_messages:
        messaged = sending_messages.pop()
        print(f"Sending message: {messaged}")
        sent_messages.append(messaged)

list_of_14_common_messages = ['BRB', 'LOL', 'OMG', 'BTW', 'IDK', 'GM', 'WSG', 'GN', 'OMW', 'OML', 'OFC', 'SMH', 'NBD', 'OM']
requested_messages_to_send = []
show_messages(list_of_14_common_messages)
send_messages(list_of_14_common_messages[:], requested_messages_to_send)  # Making a copy

print("\nFinal lists: ")
print(list_of_14_common_messages) # This list should be full with messages
print(requested_messages_to_send) # This list should be full with messages of the exact same as the starting list



# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """