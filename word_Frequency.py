word_Bank = "A,an,78,ghj,aaa,dsa,an,an,a,78"
seperated_Words = word_Bank.split(",")
print(seperated_Words)

word_dictionary = {}
for item in seperated_Words:
    if(word_dictionary.get(item)==None):
        word_dictionary[item] = 1
    else:
        word_dictionary[item] = word_dictionary[item]+1

print(word_dictionary.get("an"))