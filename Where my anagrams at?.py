def anagrams(word, words):
    list_ana = []
    list_word = list(word)
    list_word.sort()
    for i in words:
        ref = list(i)
        ref.sort()
        if list_word == ref:
            list_ana.append(i)
            
    return list_ana
