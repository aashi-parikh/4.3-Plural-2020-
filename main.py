def plural(word):
	'''Word is the string inputted by the user; this function takes the word 
    and makes it plural using the English grammar rules. It returns a string 
    that is the plural of the word.'''
	
	vowels = ['a', 'e', 'i', 'o', 'u']
	plural_word = ''
	
	if word[-1] == 's' or word[-2:] == 'ss' or word[-2:] == 'sh' or word[-2:] == 'ch' or word[-1] == 'x' or word[-1] == 'z':
		plural_word = word + 'es'
	elif word[-1] == 'y':
		if word[-2] in vowels:
			plural_word = word + 's'
		else:
			plural_word = word[0: -1] + 'ies'
	elif word[-1] == 'o':
		if word == 'photo' or word == 'piano' or word == 'halo':
			plural_word = word + 's'
		else:
			plural_word = word + 'es'
	else:
		plural_word = word + 's'
	return plural_word
print(plural('house'))
 
