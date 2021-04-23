Where my bananas/1/1//1/
	if enemy == 3:
		print('bananasss.')

	def lost():
		print('banana')
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
