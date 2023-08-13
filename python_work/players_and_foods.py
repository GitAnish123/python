players = ['charles','martina','michael','florence','eli']
print(players[0:3])
players = ['charles','martina','michael','florence','eli']
print(players[1:4])
players = ['charles','martina','michael','florence','eli']
print(players[2:4])
players = ['charles','martina','michael','florence','eli']
print(players[0:4])
players = ['charles','martina','michael','florence','eli']
print(players[-2:4])
players = ['charles','martina','michael','florence','eli']
print(players[:4])
players = ['charles','martina','michael','florence','eli']
print(players[-3:2])
players = ['charles','martina','michael','florence','eli']
print(players[:3])
players = ['charles','martina','michael','florence','eli']
print(players[:-3])
players = ['charles','martina','michael','florence','eli']
print(players[:2])
players = ['charles','martina','michael','florence','eli']
print(players[:-4])
players = ['charles','martina','michael','florence','eli']
print(players[2:])
players = ['charles','martina','michael','florence','eli']
print(players[3:])
players = ['charles','martina','michael','florence','eli']
print(players[1:])
players = ['charles','martina','michael','florence','eli']
print(players[0:])
players = ['charles','martina','michael','florence','eli']
print(players[4:])
players = ['charles','martina','michael','florence','eli']
print(players[-3:])
players = ['charles','martina','michael','florence','eli']
print(players[-1:])
players = ['charles','martina','michael','florence','eli']
print(players[-2:])
players = ['charles','martina','michael','florence','eli']
print(players[-4:])
players = ['charles','martina','michael','florence','eli']
print(players[-0:])
players = ['charles','martina','michael','florence','eli']
print(players[-3:])
# These are examples of how to slice your list.
# These tools could be very useful later on when you work with larger lists.
# There are couple syntaxes and you can do it on any index on any element.
# Make sure you don't forget "[]" this indicates a list or a list's index.
# Your lists should make sense and has all requirements, or else it won't work.
# Your lists should also follow some grammer. In these examples, I did not do any grammer work.
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())
players = ['charles','martina','michael','florence','eli']
print("Here are my last two players in my team:")
for player in players[3:5]:
    print(player.title())
    print(f"{player.title()}, you are our OG people in the league. Welcome to the team and please help me teach the others!")
# These are examples of slicing a "for" loop.