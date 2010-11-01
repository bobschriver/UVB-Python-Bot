#!/usr/bin/python

from client import Client
from constants import Action, Direction
import random
import math

# This function is called everytime the client gets a new map.
# It decides what move to make and returns the decision.
# The client module takes care of the network communication magic.
def dummy(board):
	# We need this variable to keep state between moves
	global curr_dir
	global curr_loc

	global snowballs
	global min_snowballs
	global max_snowballs
	
	global moves
	global max_moves
	global move_toggle

	# Print out our view of the game board
	print board

	possible_acts = list()
	possible_dirs = list()

	if snowballs < max_snowballs:
		for i in range(max_snowballs - snowballs):
			possible_acts.append(Action.MAKESNOWBALL)

	if snowballs < min_snowballs:
		for i in range(math.pow(2 , min_snowballs - snowballs)):
			possible_acts.append(Action.MAKESNOWBALL)
	
	player_locs = list()
	

	safe_dirs = (Direction.NORTH , Direction.SOUTH , Direction.EAST , Direction.WEST)

	for loc in board.objects:
		if board.get_object_at(loc) == board.PLAYER:
			player_loc = eval(loc)
			last_dir = curr_dir
			curr_dir = get_direction(player_loc)
			distance = get_distance(player_loc)
			print distance

			max_snowballs = 5
			min_snowballs = 2

			#moves = 0

			if distance <= 2.3:
				curr_dir = get_perp_direction(curr_dir)
			elif distance < 3 and curr_dir in safe_dirs or (distance <= 3 and curr_dir not in safe_dirs)  or (last_dir == curr_dir and curr_dir in safe_dirs and distance < 8):
				snowballs -= 1 
				return (Action.THROWSNOWBALL , curr_dir)
		elif board.get_object_at(loc) == board.SNOWBALL:
			snowball_loc = eval(loc)
			snowball_dist = get_distance(snowball_loc)
			print snowball_dist
			#if snowball_dist < 3.5:
			#	curr_dir = get_perp_direction(get_direction(snowball_loc))
		else:
			max_snowballs = 10
			min_snowballs = 3
	

			
	#print last_loc
	print curr_dir
	
	obj = board.get_object_at(board.next_pos_in_direction((0 , 0) , curr_dir)) 

	while obj:
		curr_dir += 1
		
		if curr_dir > 7:
			curr_dir = 0

		obj = board.get_object_at(board.next_pos_in_direction((0,0) , curr_dir))

	
	#last_loc = board.next_pos_in_direction((0, 0) , curr_dir)
	
	moves+=1
	return (Action.MOVE, curr_dir)

	

def get_distance(loc , curr_loc=(0,0)):
	return math.sqrt(math.pow(loc[0] , 2) + math.pow(loc[1] , 2))

def get_direction(loc , curr_loc=(0,0)):
	#global last_loc

	x_diff = curr_loc[0] - loc[0]
	y_diff = curr_loc[1] - loc[1]

	if x_diff > 0:
		#Some kind of west
		if y_diff < 0:
			return Direction.SOUTHWEST
		elif y_diff > 0:
			return Direction.NORTHWEST
		else:
			return Direction.WEST
	elif x_diff < 0:
		#Some kind of east
		if y_diff < 0:
			return Direction.SOUTHEAST
		elif y_diff > 0: 
			return Direction.NORTHEAST
		else:
			return Direction.EAST
	else:
		if y_diff > 0:
			return Direction.NORTH
		else:
			return Direction.SOUTH 

def get_slope(loc , curr_loc):
	return (curr_loc[0] - loc[0]) / (curr_loc[1] - loc[1])

def get_opposite_direction(direction):
	return (direction + 3) % 8

def get_perp_directions(direction):
	return (direction + 1) % 8

def get_possible_directions(directions , action,  order = 2 , base = 2):
	possible_directions = list() 
	for direction in directions:
		for i in range(order * -1 , order):
			possible_direction = (direction + order) % 8
			possible_order = math.pow(base , order - abs(i))

			possible_direction_tuple = (possible_direction, action)

			curr_order = possible_directions.count(possible_direction_tuple)

			if possible_order > curr_order:
				possible_order = possible_order - curr_order
				for j in range(possible_order):
					possible_directions.append(possible_direction_tuple)
	return possible_directions

# Initial direction to try to move
curr_dir = Direction.SOUTH
last_loc = ()

snowballs = 0
snowball_target = 0
min_snowballs = 3
max_snowballs = 10

moves = 0
max_moves = 100

move_toggle = True


# Create our client
c = Client()

# Insert your key here
c.KEY = "g2lVRjJN96svcwTYPG8K0MmUfdQq6Xg1" 


# Tell the client to use this function to decide the next move.
# This function is defined above.
c.decide_move = dummy

# Connect to the game server
if c.connect():
	# If we successfully connected, start playing
	print 'Connected'

	# Tell the client to start listening for maps
	c.start()

	# Wait until the user presses a key
	raw_input('Press any key to quit...')

	# Tell the client to stop listening for maps
	c.stop()

	# Wait for the client to finish its last request
	c.join()

	# Disconnect from the server
	c.disconnect()
else:
	# If we didn't successfully connected, exit
	print 'Could not connect'
