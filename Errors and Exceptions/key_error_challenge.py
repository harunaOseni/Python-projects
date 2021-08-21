# TODO:challenge 1
import pandas
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0

print(total_likes)

# TODO:challenge 2
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("Errors and Exceptions/nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)

word_is_not_found = True

while word_is_not_found:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        word_is_not_found = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
