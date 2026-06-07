dic=input("Type some words to add(use ',' for more than a word):")
dic2=dic.split(",")
while True:
    ques=input("Do you want to delete the spaces in the beginnings and endings of these words?")
    if "yes" in ques:
        dic2=[item.strip() for item in dic2]
        your_dic=dict.fromkeys(dic2,"")
        print(your_dic)
        break
    elif "no" in ques:
        your_dic=dict.fromkeys(dic2,"")
        print(your_dic)
        break
    else:
        print("Just say 'yes' or 'no'!")
while True:
    input("Press Enter to continue...")
    action=input("""What do you want to do?
'1':View all words
'2':View all meanings
'3':Add a meaning
'4':Add a word
'5':Add a word with meaning
'6':Update words with meanings
'7':Clear your dictionary
'8':Delete a word with meaning
'9':Delete the last added word with meaning(Be Careful When Using)
'10':Get the meaning of a word
'11':Get the meaning of a word, add that word if it didn't exist
'Q':Quit
Answer:""").lower()
    if action=="1":
        print(set(your_dic.keys()))
    elif action=="2":
        your_dic2=set(your_dic.values())
        if len(your_dic2)==1 and "" in your_dic2:
            print("No meaning exists!")
        else:
            print(your_dic2)
    elif action=="3":
        while True:
            word=input("Choose a word:")
            if word in your_dic.keys():
                meaning=input("Type the meaning:")
                your_dic[word]=meaning
                print(your_dic)
                break
            else:
                print("That word isn't exist!")
    elif action=="4":
        while True:
            word=input("Type the word:")
            if word in your_dic.keys():
                print("That word exists!")
            else:
                your_dic[word]=""
                print(your_dic)
                break
    elif action=="5":
        while True:
            word=input("Type the word:")
            if word in your_dic.keys():
                print("That word exists!")
            else:
                meaning=input("Type the meaning:")
                your_dic[word]=meaning
                print(your_dic)
                break
    elif action=="6":
        words=input("Type some words(use ',' for more than a word):")
        meanings=input("Type some meanings(use ',' for more than a meaning):")
        words2=words.split(",")
        meanings2=meanings.split(",")
        while True:
            ques=input("Do you want to delete the spaces in the beginnings and endings of words and meanings?").lower()
            if "yes" in ques:
                words2=[item.strip() for item in words2]
                meanings2=[item2.strip() for item2 in meanings2]
                things=list(zip(words2,meanings2))
                your_dic.update(things)
                print(your_dic)
                break
            elif "no" in ques:
                things=list(zip(words2,meanings2))
                your_dic.update(things)
                print(your_dic)
                break
            else:
                print("Just say 'yes' or 'no'!")
    elif action=="7":
        your_dic.clear()
        print(your_dic)
    elif action=="8":
        while True:
            word=input("Type the word:")
            if word in your_dic.keys():
                your_dic.pop(word)
                print(your_dic)
                break
            else:
                print("That word isn't exist!")
    elif action=="9":
        your_dic.popitem()
        print(your_dic)
    elif action=="10":
        word=input("Choose a word:")
        while True:
            ques=input("Do you want to show a default value if we can't find that word?").lower()
            if "yes" in ques:
                default=input("Type the default value:")
                your_dic2=your_dic.get(word,default)
                print(your_dic2)
                break
            elif "no" in ques:
                your_dic2=your_dic.get(word)
                if your_dic2==None:
                    print("That word isn't exist!")
                    break
                else:
                    print(your_dic2)
                    break
            else:
                print("Just say 'yes' or 'no'!")
    elif action=="11":
        word=input("Choose a word:")
        while True:
            ques=input("Do you want to add a meaning for that word if we can't find it?").lower()
            if "yes" in ques:
                meaning=input("Type the meaning:")
                your_dic2=your_dic.setdefault(word,meaning)
                if your_dic2==meaning:
                    print(your_dic)
                    break
                else:
                    print(your_dic2)
                    break
            elif "no" in ques:
                your_dic2=your_dic.setdefault(word,"")
                if your_dic2=="":
                    print(your_dic)
                    break
                else:
                    print(your_dic2)
                    break
            else:
                print("Just say 'yes' or 'no'!")
    elif action=="q":
        break
    else:
        print("Invalid answer, just type available answer!")