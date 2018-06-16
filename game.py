##guess-the-number by lemundesigns

import random, sys


def game():

	print(' How many digits? (3-10)')
	print()
	while True:
		digits = input(' > ')
		print()
		
		try:
			if int(digits) < 3 or int(digits) > 10:
				print(' Input a number between 3 and 10!')
				print()
				continue
			break
		except ValueError:
			print(' That is not a valid number!')
			print()
	print(' You have ' + str(int(digits)**2) + ' attempts to guess the number of ' + digits + ' digits!')
	print()

	number = ''
	for i in range(int(digits)):
		number += str(random.randint(0, 9))

	i = 0
	while True:

		i += 1

		if i == int(digits)**2:
			break

		print(' Try to guess! Attempt n. ' + str(i))
		print()
		while True:
			guess = input(' > ')
			print()

			try:
				int(guess)
				if len(guess) != int(digits):
					print(' You must input a number of ' + str(digits) + ' digits!')
					print()
					continue
				break
			except ValueError:
				print(' That is not a valid number!')
				print()

		if int(guess) == int(number):
			print(' Congratulations! You have guessed the number in ' + str(i) + ' attempts!')
			print()
			return
				
		clue = ' > '
		for j in range(len(guess)):

			if guess[j] == number[j]:
				clue += 'O'

			elif guess[j] in number:
				clue += 'o'

			else:
				clue += 'X'

		print(clue)
		print()

	print(' You have not guessed the number in ' + str(int(digits)**2) + ' attempts!')
	print()

def print_title():
	print()
	print(' ------------------------ Guess The Number ------------------------')
	print()
	print(' ------------------------ By lemundesigns ------------------------')
	print()
	print(' Code available at: https://github.com/lemundesigns/guess-the-number')
	print()

def start():

	while True:

		game()
		
		print(' Do you want to play again? (y/n)')
		print()
		choice = ''
		while choice != 'y' and choice != 'n':
			choice = input(' > ')
			print()
			if choice == 'n':
				exit(0)

print_title()

start()
