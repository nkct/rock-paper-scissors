
import random

print('This is Rock Paper Scisors. \n Welcome.\n Type \"help\" to get help.')

sum = 0
player = 0
loses = 0
wins = 0
streak = 0

while True:

	player_input = input('Input command:')

	enemy = random.randrange(1,4)

	if player_input == 'help':
		print('\n Commands avialble:\n [scissors] or [s] to play scissors \n [rock] or [r] to play rock \n [paper] or [p] to play paper \n \n [stats] to display streak, sum of wins and w/l ratio\n ')
	
	elif player_input == 'stats':
		print("Wins: ", wins)
		print("Loses: ", loses)
		print('Streak:', streak)
		print('Sum of wins:', sum)
		try:
			print('Win ratio:', wins/loses)
		except ZeroDivisionError:
			print('You need to play a few games before displaying Win Ratio.')
	
	elif player_input == 'scissors':
		player = 1
	elif player_input == 's':
		player = 1
	
	elif player_input == 'rock':
		player = 2
	elif player_input == 'r':
		player = 2
		
	elif player_input == 'paper':
		player = 3
	elif player_input == 'p':
		player = 3
	
	else:
		print('InputError; Unrecognised Input')
		continue
	if enemy == 1:
		print('Your enemy choose Scissors.')
	
	if enemy == 2:
		print('Your enemy choose Rock.')
	
	if enemy == 3:
		print('Your enemy choose Paper.')

	def lost():
		print('You Lost!')
		global sum
		global loses
		global streak
		sum -= 1
		loses += 1
		if streak >= 0:
			streak = 0
			streak -= 1
		else:
			streak -= 1

	def won():
		print('You Won!')
		global sum
		global wins
		global streak
		sum += 1
		wins += 1
		if streak <= 0:
			streak = 0
			streak += 1
		else:
			streak += 1
	
	if player == enemy:
		print("Tie!")
		continue

	if player == 1:
		if enemy == 2:
			lost()
		if enemy == 3:
			won()

	if player == 2:
		if enemy == 1:
			won()
		if enemy == 3:
			lost()

	if player == 3:
		if enemy == 1:
			lost()
		if enemy == 2:
			won()
