"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    n = 1 
    # str = ''
    list_length = len(vocab_words)
    new_list = [vocab_words[0], ' :: ']
    
    for x in vocab_words:
        if n < list_length-1:
            new_list += [vocab_words[0] + vocab_words[n], ' :: ']
            n += 1
        else:
            new_list += [vocab_words[0] + vocab_words[n]] #why did adding a str or changing to brackets help adding to this to the list
            break
    # print(new_list)
    str = ''.join(new_list) #wtf is this .join function and it has to have something empty for it to go into?
    # print(str)

    # prefix = vocab_words[0]
    # first_word = vocab_words[1]
    # n = len(vocab_words)
    # last_word = vocab_words[n-1]   
    return str


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    word_length = len(word)
    new_word = word[0:word_length-4]
    new_length = len(new_word)

    if 'i' == new_word[new_length-1]:
        new_word = new_word.replace('i', 'y')

    return new_word

    


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """
    list = sentence.split(' ')
    word = list[index]
    length = len(word)
    if word[length-1] == '.':
        verb = word.replace('.', 'en')
    else: 
        verb = word + 'en'
    
    # word = ''
    # n = 0

    # for x in list:
    #     word += list[index-n]
    #     n += 1
    #     print(word)
    #     if list[index-n] == ' ':
    #         break

    # print(word)
    return verb





# vocab_words = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
# make_word_groups(vocab_words)
# remove_suffix_ness('heaviness')
adjective_to_verb('His expression went dark.', -1)