def valid_word_abbreviation(word, abbr):

    # Replace the following return statement with your code
    if (len(word) > 20 or len(word) <1 ) or (len(abbr) >10 or len(abbr) <1):
        return False

    missing_numbers = list()
    alpha_numbers = 0
    i=0
    w=0
    while i < len(abbr):
        skip_next = False

        if abbr[i].isdigit():

            if abbr[i] == "0":
                return False

            temp = abbr[i]                                   # CHANGED: start the number with the first digit
            while i+1 < len(abbr) and abbr[i+1].isdigit():   # CHANGED: "if" became "while", keep reading digits
                temp += abbr[i+1]                            # CHANGED: add the next digit onto the number
                i+=1

            missing_numbers.append(temp)
            w += int(temp)                    # jump ahead in word by the whole number

        else:
            if w >= len(word) or word[w] != abbr[i]:   # ADDED: letter must match word at position w
                return False                           # ADDED
            w += 1                                     # ADDED: move to the next character of word
            alpha_numbers +=1
        i+=1


    print("number ", missing_numbers)
    total = 0
    for i in missing_numbers:
        total += int(i)

    print("Total = ",total, "alpha numbers = ",alpha_numbers, "  sum = ", total + alpha_numbers)

    if len(word) == (total + alpha_numbers):
        return True
    else:
        return False




print(valid_word_abbreviation("internationalization", "i12iz4n"))  # True
# print(valid_word_abbreviation("apple", "a3e"))                     # True
# print(valid_word_abbreviation("apple", "a2e"))                     # False
print(valid_word_abbreviation("substitution", "s10n"))             # True
# print(valid_word_abbreviation("word", "4"))                        # True
# print(valid_word_abbreviation("word", "w2d"))                      # True
print(valid_word_abbreviation("word", "w3"))                       # True
print(valid_word_abbreviation("word", "5"))                        # False
print(valid_word_abbreviation("apple", "a01e"))                    # False
print(valid_word_abbreviation("apple", "b3e"))                     # False
print(valid_word_abbreviation("apple", "a3x"))                     # False
print(valid_word_abbreviation("word", "w9d"))                      # False
print(valid_word_abbreviation("abcdefghijklmno", "132"))           # False
