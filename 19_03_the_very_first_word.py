def first_word(text):
    """ Пошук першого слова """
    for potential_first_letter in range(len(text)):
        if text[potential_first_letter].isalpha():
            first_letter = potential_first_letter
            break
    else:
        return ''
    
    for potential_end_letter in range(first_letter, len(text)):
        if not (text[potential_end_letter].isalpha() or text[potential_end_letter] == "'" or text[potential_end_letter] == "`"):
            return text[first_letter:potential_end_letter]
    
    return text[first_letter:]
  
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
# added two additional asserts to check for words with apostrophes and backticks
assert first_word("V`iacheslav") == "V`iacheslav", 'Test7'
assert first_word("V'iacheslav") == "V'iacheslav", 'Test8'

print('OK')