from dictionary import Dictionary


class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print(f'------------------------------')
        print(f'  Translator Alien-Italian  ')
        print(f'------------------------------')
        print(f'1. Aggiungi nuova parola')
        print(f'2. Cerca una traduzione')
        print(f'3. Cerca con wildcard')
        print(f'4. Stampa tutto il Dizionario')
        print(f'5. Exit')
        print(f'-------------------------------')

    def loadDictionary(self, dict):
        dizionario = {}
        with open(dict, 'r') as file:
            linee = file.readlines()
            for linea in linee:
                chiave, valore = linea.strip().split()
                dizionario[chiave] = valore
        # dict is a string with the filename of the dictionary
        diz = Dictionary(dizionario)
        return diz

    def handleAdd(self, entry, dict):
        dizionario = Dictionary(dict)
        dizionario.addWord(entry)
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query, dict):
        dizionario = Dictionary(dict)
        dizionario.translate(query)
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass