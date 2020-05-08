from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     description= "North of you, the cave mount beckons", items =[sword]),

    'foyer':    Room("Foyer",
    decription = """Dim light filters in from the south. Dusty
passages run north and east.""" items=[candle]),

    'overlook': Room("Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""items=[compass]),

    'narrow':   Room("Narrow Passage", description = """The narrow passage bends here from west
to north. The smell of gold permeates the air.""" items=[water]),

    'treasure': Room("Treasure Chamber", description= """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""" items=[gold])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player = Player ("Zac", room ['outside'])

sword = Item("sword")
candle =Item("candle")
compass = Item("compass")
water = Item("water")
gold = Item("gold")
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
def find_key(value, my_dict):
    key_list = list(my_dict.keys())
    value_list = list(my_dict.values())
    return key_list[value_list.index(value)]

#
# * Prints the current room name
while True:

print('\n','You are in  {}'.format(player.location), '\n')
    room[player.location].get_items()
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user_input = input('Please enter a direction, n,s,w or e, to exit please enter "quit"): ')
if command == "quit":
    break
  
  if user_input == 'n':
        print('\n', 'you selected north')
        if  room[player.location].s_to != None:
            player.location = find_key(room[player.location].s_to, room)
            print('\n',f'now you are in{player.location}')
            room[player.location].get_items()
        else: 
            print('\n', 'oh oh can not go that way , please enter another direction')

    elif user_input == 's':
        print('\n', 'you selected south')
        if room[player.location].n_to != None:
            player.location = find_key(room[player.location].n_to, room)
            print('\n',f'now you are in{player.location}')
        else:
             print('\n', 'oh oh can not go that way , please enter another direction')
    elif user_input == 'e':
        print('\n', 'you selected east')
        if room[player.location].w_to != None:
            player.location = find_key(room[player.location].w_to, room)
            print('\n',f'now you are in {player.location}')
        else:
             print('\n', 'oh oh can not go that way , please enter another direction')
            
    elif user_input == 'w':
        print('\n', 'you selected west')
        if room[player.location].e_to != None:
            player.location = find_key(room[player.location].e_to, room)
            print('\n',f'now you are in{player.location}')
        else:
             print('\n', 'oh oh can not go that way , please enter another direction')
    else:
        print('I can not undestand, try again') 