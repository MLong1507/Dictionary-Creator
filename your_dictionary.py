dic=input("Type some words to add(use ',' for more than a word):")
dic2=dic.split(",")
while True:
    ques=input("Do you want to set a default meaning for these words?").lower()
    if "yes" in ques:
        defmean=input("Type the meaning:")
        your_dic=dict.fromkeys(dic2,defmean)
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
'6':Clear your dictionary
'7':Delete a word with meaning
'8':Delete the last added word with meaning(Be Careful When Using)
'9':Get the meaning of a word
'10':Get the meaning of a word, add that word if it didn't exist
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
        your_dic.clear()
        print(your_dic)
    elif action=="7":
        while True:
            word=input("Type the word:")
            if word in your_dic.keys():
                your_dic.pop(word)
                print(your_dic)
                break
            else:
                print("That word isn't exist!")
    elif action=="8":
        your_dic.popitem()
        print(your_dic)
    elif action=="9":
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
    elif action=="10":
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