import string

print("Welcome to the hashtag generator!")
print("Please enter a phrase and we will convert it into a hashtag for you.")
potential_hashtag = input("Enter a phrase to make hashtag: ")

if not potential_hashtag:
    print("You entered an empty string. Please enter a valid phrase.")
else:
    # remove punctuation
    potential_hashtag_with_no_punctuation = ''.join(char for char in potential_hashtag if char not in string.punctuation)
    # split the phrase into words, capitalize each word and join them together
    hashtag = '#' + ''.join(word.capitalize() for word in potential_hashtag_with_no_punctuation.split())
    # cut the hashtag to 140 characters if it's too long
    hashtag = hashtag[:140]

    print("Your hashtag is:", hashtag)