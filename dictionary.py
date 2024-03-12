class Dictionary:
    def __init__(self, dict):
        self.dict = dict

    def __str__(self):
        dizionario = {}
        with open(self, 'r') as file:
            linee = file.readlines()
            for linea in linee:
                dizionario[linea.split(" ")[0]] = dizionario[linea.split(" ")[1]]
        # dict is a string with the filename of the dictionary
        for chiave in dizionario:
            valore = dizionario[chiave]
            print(f"{chiave} {valore}")

    def addWord(self, entry):
        alieno = entry.strip().split()[0]
        umano = entry.strip().split()[1]
        with open("dictionary.txt", 'a') as file:
            daAggiungere = alieno+" "+umano
            file.write(daAggiungere)
        pass

    def translate(self, query):
        with open(self, 'r') as file:
            linee = file.readlines()
            for linea in linee:
                if ( linea.split(" ")[0] == query):
                    return linea.split(" ")[1]
        pass

    def translateWordWildCard(self):
        pass

