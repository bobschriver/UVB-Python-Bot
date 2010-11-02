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
	
	global min_player_distance

	global max_throw_snowball_distance

	# Print out our view of the game board
	print board

	possible_moves = list()

	if snowballs < max_snowballs:
		for i in range(max_snowballs - snowballs):
			possible_moves.append((Action.MAKESNOWBALL , curr_dir))

	if snowballs < min_snowballs:
		for i in range(math.pow(2 , min_snowballs - snowballs)):
			possible_moves.append((Action.MAKESNOWBALL , curr_dir))
		

	#replace with the curr_loc + direction at some point
	for loc in board.objects:
		if board.get_object_at(loc) == board.ME:
			curr_loc = eval(loc)		

	player_locs = list()

	for loc in board.objects:
		if board.get_object_at(loc) == board.PLAYER:
			player_loc = eval(loc)
			player_locs.append(player_loc)
	
			player_dir = get_direction(player_loc)
			player_dist = get_distance(player_loc)
			#player_slope = math.abs(get_slope(player_loc))

			print player_dist
			
			if player_dist <= min_player_distance:
				possible_directions = get_possible_directions([get_opposite_direction(player_dir)] , Action.MOVE , order = 1 , base = 20)
				possible_moves.extend(possible_directions)
			else:
				possible_directions = get_possible_directions([player_dir] , Action.MOVE , order = 2, base = 3)
				possible_moves.extend(possible_directions)
			
			if player_dist <= max_throw_snowball_distance:
				possible_directions = get_possible_directions([player_dir] , Action.THROWSNOWBALL , order = 1 , base = 6 + max_throw_snowball_distance - player_dist)
				possible_moves.extend(possible_directions)


	#TODO: implement snowball tracking
	#tmp_snowball_locs = dict()

	#for snoball_loc, snowball_dir  in snowball_locs:
	#	snowball_loc = get_next_location(snowball_loc , snowball_dir)
	#	if board.get_object_at(snowball_loc) == board.SNOWBALL:
	#		tmp_snowball_locs[snowball_loc] = snowball_dir
	

	possible_moves.extend(get_possible_directions([curr_dir] , Action.MOVE , order = 3 , base = 2))

	print possible_moves

	possible_move = random.choice(possible_moves)

	while possible_move:
		possible_action = possible_move[0]
		possible_direction = possible_move[1]

		if possible_action == Action.MOVE or possible_action == Action.THROWSNOWBALL:
			object = board.get_object_at(board.next_pos_in_direction((0,0) , possible_direction))
			if object:
				possible_move = random.choice(possible_moves)
				continue
			else:
				if possible_action == Action.THROWSNOWBALL:
					snowballs -= 1
				curr_dir = possible_direction
				return possible_move
		elif possible_action == Action.MAKESNOWBALL:
			snowballs += 1
			curr_dir = possible_direction
			return possible_move

	

def get_distance(loc , curr_loc=(0,0)):
	return math.sqrt(math.pow(loc[0] - curr_loc[0] , 2) + math.pow(loc[1] - curr_loc[1], 2))

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

def get_slope(loc , curr_loc = (0,0)):
	if curr_loc[1] - loc[1] == 0:
		return 0
	else:
		return (curr_loc[0] - loc[0]) / (curr_loc[1] - loc[1])

def get_opposite_direction(direction):
	return (direction + 3) % 8

def get_perp_directions(direction):
	return (direction + 1) % 8

def get_possible_directions(directions , action,  order = 2 , base = 2):
	possible_directions = list() 
	for direction in directions:
		for i in range(order * -1 , order):
			#print i , direction
			possible_direction = (direction + i) % 8
			possible_order = math.pow(base , order - abs(i))

			#print possible_direction , possible_order

			possible_direction_tuple = (action , possible_direction)

			curr_order = possible_directions.count(possible_direction_tuple)

			if possible_order > curr_order:
				possible_order = possible_order - curr_order
				for j in range(possible_order):
					#print possible_direction_tuple
					possible_directions.append(possible_direction_tuple)
	return possible_directions

# Initial direction to try to move
curr_dir = Direction.SOUTH
last_loc = ()

snowballs = 0
snowball_target = 0
min_snowballs = 3
max_snowballs = 10

min_player_distance = 3.5

max_throw_snowball_distance = 6


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
