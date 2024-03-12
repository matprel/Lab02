import translator as tr
from dictionary import Dictionary

t = tr.Translator()

while(True):

    t.printMenu()

    d = t.loadDictionary("dictionary.txt")

    txtIn = input()
    if txtIn.isalpha():
        continue
    # Add input control here!

    if int(txtIn) == 1:
        print(f'Ok, quale parola devo aggiungere?')
        txtIn = input()
        t.handleAdd(txtIn.lower(), d)

    if int(txtIn) == 2:
        print('Ok, quale parola devo cercare?')
        txtIn = input()
        t.handleTranslate(txtIn.lower(), d )
        pass
    if int(txtIn) == 3:
        print('Ok, quale parola devo cercare?')
        txtIn = input()
        pass
    if int(txtIn) == 4:
        d.__str__()
    if int(txtIn) == 5:
        break
