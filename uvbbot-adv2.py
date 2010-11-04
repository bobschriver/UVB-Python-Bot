#!/usr/bin/python

from client import Client
from constants import Action, Direction
import random
import math
import sys

# This function is called everytime the client gets a new map.
# It decides what move to make and returns the decision.
# The client module takes care of the network communication magic.
def dummy(board):
	# We need this variable to keep state between moves
	global curr_dir
	global curr_loc

	global snowball_locs

	global snowballs
	global min_snowballs
	global max_snowballs
	
	global min_player_distance

	global max_throw_snowball_distance

	# Print out our view of the game board
	print board

	possible_moves = list()

	if snowballs < min_snowballs:
		max_snowballs = 7
		possible_moves.append((Action.MAKESNOWBALL , curr_dir))

	#replace with the curr_loc + direction at some point
	for loc in board.objects:
		if board.get_object_at(loc) == board.ME:
			curr_loc = eval(loc)		

	player_locs = list()

	closest_player_loc = ()
	closest_player_slope = 0
	closest_player_dir = 0
	closest_player_dist = sys.maxint

	for loc in board.objects:
		if board.get_object_at(loc) == board.PLAYER:
			player_loc = eval(loc)
			player_locs.append(player_loc)
	
			player_dir = get_direction(player_loc)
			player_dist = get_distance(player_loc)
			player_slope = get_slope(player_loc)
			

			print "Player Dist:" , player_dist," Player Slope:" , player_slope
			
			if player_dist < closest_player_dist:
				closest_player_dist = player_dist
				closest_player_dir = player_dir
				closest_player_slope = player_slope
				closest_player_loc = player_loc
	
	print "Closest Player Location " , closest_player_loc , " Closest Player Distance " ,  closest_player_dist , " Closest Player Dir " , closest_player_dir , " Closest Player Slope " , closest_player_slope
	print "Curr Dir:" , curr_dir

	if closest_player_loc:
		if closest_player_dist <= min_player_distance:
			possible_directions = get_possible_directions(get_opposite_diagonal_directions(closest_player_dir) , Action.MOVE , order = 1)
			possible_moves.extend(possible_directions)
		elif (closest_player_dist <= max_throw_snowball_distance or curr_dir == closest_player_dir) and (abs(closest_player_slope) == 1 or abs(closest_player_slope) == 0):
			possible_directions = get_possible_directions([closest_player_dir] , Action.THROWSNOWBALL , order = 1)
			possible_moves.extend(possible_directions)
		else:	
			print " Closest Player Dir:" , closest_player_dir
			possible_moves.extend(get_possible_directions([closest_player_dir] , Action.MOVE , order = 2))

	#TODO: implement snowball tracking
	
	tmp_snowball_locs = dict()

	for (snowball_loc) , snowball_dir in snowball_locs.iteritems():
		print "Snowball Loc: " , snowball_loc , " Snowball Dir: ",  snowball_dir
		snowball_loc = board.next_pos_in_direction(snowball_loc , snowball_dir, amount = 2)
		if board.get_object_at(snowball_loc) == board.SNOWBALL:
			tmp_snowball_locs[snowball_loc] = snowball_dir

	snowball_locs = tmp_snowball_locs

	#Fix this to deal with Rougue snowballs
	for loc in board.objects:
		if board.get_object_at(loc) == board.SNOWBALL:
			snowball_loc = eval(loc)
			if snowball_loc not in snowball_locs:
				min_player_dist = sys.maxint
				closest_player_loc = ()
				for player_loc in player_locs:
					player_dist = get_distance(snowball_loc , player_loc)
					player_slope = get_slope(snowball_loc , player_loc)
					player_slope = abs(player_slope)

					if player_dist < min_player_dist and player_loc != curr_loc and (player_slope == 1 or player_slope == 0):
						print "Player Dist" ,  player_dist , " Player Loc " , player_loc , " Player Slope " , player_slope
						min_player_dist = player_dist
						closest_player_loc = player_loc
				if closest_player_loc:
					snowball_dir = get_direction(snowball_loc , closest_player_loc)
					print "Snowball Loc " , snowball_loc , " Snowball Dir " ,  snowball_dir
					snowball_locs[snowball_loc] = snowball_dir



	avoid_locs = []
	
	#Fix this to something better once collision is understood
	for (snowball_loc), snowball_dir in snowball_locs.iteritems():
		print snowball_loc , snowball_dir
		avoid_locs.append(snowball_loc)
		avoid_locs.append(board.next_pos_in_direction(snowball_loc , snowball_dir))
		avoid_locs.append(board.next_pos_in_direction(snowball_loc , snowball_dir, amount = 2))
	
	if snowballs < max_snowballs:
		possible_moves.append((Action.MAKESNOWBALL , curr_dir))
	else:
		max_snowballs = 0

	possible_moves.extend(get_possible_directions([curr_dir] , Action.MOVE , order = 4))

	print possible_moves

	for possible_move in possible_moves:
		possible_action = possible_move[0]
		possible_direction = possible_move[1]

		if possible_action == Action.MOVE:
			#Moving Action

			#TODO Add all non-player pieces to avoid_locs
			possible_next_loc = board.next_pos_in_direction((0, 0) , possible_direction)
			object = board.get_object_at(possible_next_loc)
			if object or possible_next_loc in avoid_locs:
				continue
			else:
				curr_dir = possible_direction

				for snowball_loc, snowball_dir in snowball_locs.iteritems():
					snowball_loc = board.next_pos_in_direction(snowball_loc , get_opposite_direction(curr_dir))

				return possible_move
		elif possible_action == Action.THROWSNOWBALL:
			if snowballs > 0 and  check_snowball_path(board , possible_direction , curr_loc) and curr_loc not in avoid_locs:
				print "Throwing Snowball", possible_direction
				curr_dir = possible_direction
				print curr_loc , curr_dir
				snowball_locs[curr_loc] = curr_dir		
				snowballs -= 1
				return possible_move
		elif possible_action == Action.MAKESNOWBALL:
			if curr_loc not in avoid_locs:
				curr_dir = possible_direction
				snowballs += 1
				return possible_move


def get_distance(loc , curr_loc=(0,0)):
	#return math.sqrt(math.pow(loc[0] - curr_loc[0] , 2) + math.pow(loc[1] - curr_loc[1], 2))
	#return abs(loc[0] - curr_loc[0]) + abs(loc[1] - curr_loc[1])
	x_diff = abs(loc[0] - curr_loc[0])
	y_diff = abs(loc[1] - curr_loc[1])

	return max(x_diff , y_diff)

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
		return float((curr_loc[0] - loc[0])) / float((curr_loc[1] - loc[1]))

def get_opposite_direction(direction):
	return (direction + 4) % 8

def get_opposite_diagonal_directions(direction):
	return [(direction + 3 ) % 8 , (direction + 5) % 8]

def get_perp_directions(direction):
	return (direction + 1) % 8

def get_possible_directions(directions , action,  order = 2):
	possible_directions = [] 
	for i in range(order):
		for direction in directions:
		#print i , direction
			possible_direction = (direction + i) % 8
			possible_direction_opp = (direction - i + 8) % 8

			possible_direction_tuple = (action , possible_direction)
			possible_direction_opp_tuple = (action, possible_direction_opp)

			if possible_direction_tuple not in possible_directions:
				possible_directions.append(possible_direction_tuple)
			
			if possible_direction_opp_tuple not in possible_directions:
				possible_directions.append(possible_direction_opp_tuple)

	return possible_directions

def check_snowball_path(board , direction, curr_loc = (0,0)):
	for i in range(8):
		object = board.get_object_at(board.next_pos_in_direction(curr_loc , direction, i))
		if object == board.TREE or object == board.SNOWMAN:
			return False
		elif object == board.PLAYER:
			return True

def adjust_distance(distance , slope):
	slope = abs(slope)
	if slope != 0:
		return distance / math.sqrt(2)
	else:
		return distance

# Initial direction to try to move
curr_dir = Direction.NORTH
curr_loc = (0 , 0)
snowball_locs = dict()

snowballs = 0
snowball_target = 0
min_snowballs = 3
max_snowballs = 10

min_player_distance = 3# * math.sqrt(2)

max_throw_snowball_distance = 5# * math.sqrt(2)


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
