import random
options = ['R', 'P', 'S']
dic = {'R' : 'Rock' , 'P' : 'Paper', 'S' : 'Scissors'}

move = {}

def game_play():
	isvalidoption = False
	while isvalidoption == False :
		p1_sel = input('make a valid selection: R ---> Rock ; P ---> Paper ; S ---> Scissors \n')
		if p1_sel not in options:
			print('Error in selection')
		else:
			move['player'] = p1_sel
			isvalidoption = True
			
	cpu_sel = random.choice(options)
#cpu random selection

	move['cpu'] = cpu_sel
	print('Player (%s) : CPU (%s)' %(dic[p1_sel], dic[cpu_sel]))
	if (move['player'] == 'R') and (move['cpu'] == 'S'):
		print('player wins')
	elif (move['player'] == 'S') and (move['cpu'] == 'R'):
		print('cpu wins')
	elif (move['player'] == 'P') and (move['cpu'] == 'R'):
		print('player wins')
	elif (move['player'] == 'R') and (move['cpu'] == 'P'):
		print('cpu wins')
	elif (move['player'] == 'S') and (move['cpu'] == 'P'):
		print('player wins')
	elif (move['player'] == 'P') and (move['cpu'] == 'S'):
		print('cpu wins')
	else:
		game_play()


game_play()
	
