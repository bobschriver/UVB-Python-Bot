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
	global last_loc

	global snowballs
	global snowball_target
	global min_snowballs
	global max_snowballs
	
	global moves
	global max_moves

	# Print out our view of the game board
	print board

	if snowballs < snowball_target:
		snowballs += 1
		return (Action.MAKESNOWBALL, curr_dir)
	else:
		snowball_target = 0
	
	if snowballs < min_snowballs:
		snowball_target = max_snowballs

	if not last_loc:
		for loc in board.objects:
			if board.get_object_at(loc) == board.ME:
				print loc
				last_loc = loc
	

	distance = 0

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

			moves = 0

			if distance < 3:
				curr_dir = get_opposite_direction(curr_dir)
			elif distance < 4 or (last_dir == curr_dir and curr_dir in safe_dirs and distance < 8):
				snowballs -= 1 
				return (Action.THROWSNOWBALL , curr_dir)
		elif board.get_object_at(loc) == board.SNOWBALL:
			snowball_loc = eval(loc)
			curr_dir = get_perp_direction(get_direction(loc))
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
	
	if moves > max_moves:
		return (Action.MAKESNOWBALL , curr_dir)

	moves+=1
	return (Action.MOVE, curr_dir)

	

def get_distance(loc , curr_loc):
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

def get_perp_direction(direction):
	return direction + 1

# Initial direction to try to move
curr_dir = Direction.SOUTH
last_loc = ()

snowballs = 0
snowball_target = 0
min_snowballs = 3
max_snowballs = 10

moves = 0
max_moves = 100


# Create our client
c = Client()

# Insert your key here
c.KEY = "" 


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
