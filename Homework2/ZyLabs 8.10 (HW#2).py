# Will Buckner Jr#
# PS_ID: 2101260#
def palindrome_test(word):
    joining = ''
    new_word = word.split()
    new_word = joining.join(new_word)
    backwards = []
    for x in new_word:
        backwards.insert(0, x)
    backwards = joining.join(backwards)
    if new_word == backwards:
        return print(f"{word} is a palindrome")
    else:
        return print(f"{word} is not a palindrome")


word_test = input()
palindrome_test(word_test)
