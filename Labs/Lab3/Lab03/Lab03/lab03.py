VOWELS = "aeiou"
while True:
    word = input(":~Enter a word ('quit' to quit)~:")
    if len(word) == 0:
        print("Can't convert an empty string. Try again.")
        continue
        
# Error message used in Codio test
#print("Can't convert an empty string. Try again.")
    
    word = word.lower()
    if word == "quit":
        break
    if word[0] in VOWELS:
        word = word + "way"
        print(word)
        continue

    for i in word:
        if word[0] not in VOWELS:
            word = word[1:]+word[0]
    word=word+"ay"
    print(word)


    
