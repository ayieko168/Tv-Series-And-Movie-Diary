
def search_the_word(word_dict, search_word):
    """word_dict => a list of words to search from.
       search_word => a word to search for in the provided list.
        USAGE:
           This function is used to search for a word in a list of provided
           list of other words. It proviides a mathch according to the accuracy
           of similar matches found in the list
        RETURN:
            The function returns a dictionary of two keys:
                do_you_mean = Containing a
                 list of possible matches to the sugested word.
                match = Contains a string value of the match found, it is empty string
                 if no matches are found.
    """
    results = {"do_you_mean": [], "match": ""}
    i = 0
    total = 0
    do_you_mean = []
    match = None

    if search_word != "":
        for word in word_dict:
            """go through each word in the word dictionary"""

            # clean the words ie: remove punctuation
            curentWord = word
            word = word.strip(",.\'\"!@#$%?<>^&*()_+/*-+").lower().replace(" ", "")
            search_word = search_word.strip(",.\'\"!@#$%?><^&*()_+/*-+").lower().replace(" ", "")

            #break the dictinary word to a list of letters
            word_letters = list(word)
            #break the search word to a list fo letters 
            search_word_letters = list(search_word)

            try:
                for x in search_word_letters:
                    """look if the i'th letter of the dict word mathces to the search word"""
                    if x == word_letters[i]:
                        # if they match, incerase the confidence score
                        total+=1
                    else:
                        total = total + 0
                        # if no match, do nothing to the confidence score
                    i+=1
            except:
                pass
            
            percentage_score = (total*100)/len(search_word) # the confidece score in percentage

            if (percentage_score >= 95) and (word.startswith(search_word)):
                match = curentWord
            elif (percentage_score >=50) and (percentage_score < 100) and ((len(search_word) <= ((len(word)+2)) or (len(search_word) >=(len(word)-2)))):
                do_you_mean.append(curentWord)
            elif percentage_score <=10:
                pass

            # reset the i'th and total values to check the next dictionary word
            i = 0
            total = 0

        # print the list of close words OR any match found
    ##    print("do you mean :: ", do_you_mean)
    ##    print("match :: ", match)

        results["do_you_mean"] = do_you_mean
        results["match"] = match

        return results
