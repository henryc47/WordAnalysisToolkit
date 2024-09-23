#words list from https://github.com/dwyl/english-words/blob/master/words.txt

def get_word_list(filename):
    words = []
    file = open(filename)
    for line in file:
        words.append((line.rstrip()).lower())
    return words

def word_matches(word,match_string):
    match_string_length = len(match_string)
    word_length = len(word)
    if word_length!=match_string_length:
        return False
    for i,match_chr in enumerate(match_string):
        if match_chr=="*":#wildcat character
            continue
        else:
            if match_chr!=word[i]:
                return False
    return True


def get_matching_words(words,match_string):
    matches = []
    for word in words:
        if word_matches(word,match_string):
            matches.append(word)
    return matches

if __name__=="__main__":
    words = get_word_list("words.txt")
    while True:
        user_input = input("type in match string :")
        if user_input =="$exit":
            break
        else:
            matches = get_matching_words(words,user_input)
            print("matches are \n",matches)





