try:
    while True:
        sentence = ''
        mod_sent=''
        modsent2 =""
        num = 0
        num2 = 0
        num3 = 0
        num4 = 0
        comb=[]
        nospace = str()
        numoflet = 0
        var2 = str()
        list2= []
        len2 = 0
        cond4 = 0
        var = []
        altvar = []
        cond3=0


        while len(sentence) == 0:
            sentence = input("enter a sentence:")

        for i in sentence:
            if i == ' ':
                num += 1
            elif not i == ' ':
                break
        sentence = (sentence[num:])

        for x in sentence[::-1]:

            if x == ' ':
                num2 += 1

            elif not x == ' ':
                break
        if num2 == 0:
            sentence = sentence[:]
        else:
            sentence = sentence[:-num2]

        for k in sentence:
            if k != ' ':
                nospace = nospace + k

        nospace = set(nospace)
        for w in nospace:
            numoflet += sentence.count(" " + w)

        for p in nospace:
            if p != ' ':
                num3 = 1

        if num3 == 1:
            numoflet = numoflet+1
            print(f"No. of words: {numoflet}\n")
        else:
            numoflet = 0
            print(f"No. of words:{0}\n")
#______________making list_____________________
        mod_sent = sentence + " "
        for words3 in mod_sent:
            if words3 != ' ':
                var2 = var2 + words3
            else:
                list2.append(var2)
                var2 = str()
        list2 = set(list2)
        list2 = list(list2)





#______________longest word______________
        while cond3 < 2:#to make everything under it run twice [cond3 increments by 1 with each round if certain conditions are met]
            if numoflet>1:#checks if number of words in sentence is more than 1

                for word in list2:#word taken to compare with the rest
                    for word2 in list2:

                        if word != word2:#checks if the same elements are being compared
                            if len(word) > len(word2):
                                len2 += 1

                            elif len(word) == len(word2):
                                var.append(word2)#word2 will be the value of a variable called 'var'
                                cond4 = 1#if there are elements with the same length, this variable becomes 1
                                len2 += 1

                            else:#if the 'word2' is smaller than 'word'
                                var = []
                                len2 = 0
                                cond4 = 0
                                break


                        else:
                            len2 += 1

                    if cond4==1:
                        if len2==len(list2):
                            if cond3 == 0:
                                var.append(word)
                                var = set(var)#gets rid of duplicate values
                                var = list(var)#turns it into list again
                                altvar = var#assigns the value to an alternate variable to clear 'var'
                                print("the longest words are:",var)
                                var = []
                                cond4=0
                                len2=0
                                break

                            else:
                                var.append(word)
                                print("the second longest words are:", var)
                                break
                        else:
                            pass




                    else:
                        if len2 == len(list2):
                            if cond3 == 0:
                                print("The longest word is:", word)
                                len2 = 0
                                list2.remove(word)

                            else:
                                print("The second longest word is:", word)
                                len2 = 0

                            break
                        else:
                            pass

            elif numoflet==1 :
                print("There is only 1 word\nNumber of letters in the word is:", len(sentence))
                cond3 = 2

            else:
                print("there are no words.")
                cond3 = 2
            # _________________no. of letters in each_______________________

            if numoflet>1:
                if cond3 == 0:
                    cond3 += 1
                    print("The number of letters in the longest word(s):", len(word),"\n")
                    for xy in altvar:
                        if xy in list2:
                            list2.remove(xy)
                else:
                    if len(list2)>0:
                        cond3 += 1
                        print("the number of letters in the second longest word(s):",(len(word)))
                    else:
                        cond3+=1

#BUG: when 2 same words are entered, the number of letters in the longest word is not showing






except KeyboardInterrupt:
    print("\n🔴The code has been stopped🔴")