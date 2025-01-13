# Program to Generate a strong random password

# import modules
import string
import random


# store all characters in lists 
small_letters = list(string.ascii_lowercase)
cap_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
punc = list(string.punctuation)


# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")


# checking the user_input is number or not
while True:

	try:

		characters_number = int(user_input)

		if characters_number < 8:

			print("Your number should be at least 8.")

			user_input = input("Please, Enter your number again: ")

		else:

			break

	except:

		print("Please, Enter numbers only.")

		user_input = input("How many characters do you want in your password? ")


# shuffle all lists
random.shuffle(small_letters)
random.shuffle(cap_letters)
random.shuffle(numbers)
random.shuffle(punc)


# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):

	result.append(small_letters[x])
	result.append(cap_letters[x])

for x in range(part2):

	result.append(numbers[x])
	result.append(punc[x])


# shuffle result
random.shuffle(result)


# join result
password = "".join(result)
print("Strong Password: ", password)
