def first_word(input_word):
   second_word = input_word.replace(',', '').replace('.', ' ').strip().split()
   return second_word[0]

print(first_word("don't touch it"))