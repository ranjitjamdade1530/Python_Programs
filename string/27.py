text = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word.lower() in text.lower().split():
    print("Word exists in the sentence")
else:
    print("Word does not exist in the sentence") 