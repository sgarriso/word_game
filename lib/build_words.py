from PyDictionary import PyDictionary

dictionary=PyDictionary()
class Word:
    def __init__(self,word,wordtype,meaning):
        self.word = word
        self.wordtype = wordtype
        self.meaning = meaning
        self.__file__()
    def __file__(self,file='pythonword.txt'):
        with open(file,'a+') as f:
            output=self.__str__()
            f.write(output)
            f.write("\n")
    def __str__(self):
        return self.word + str(self.wordtype) + str(self.meaning)

def read_file(file = 'words.txt'):
    with open(file) as f:
        read_data = f.readlines()
    return read_data
def build_words():
    data=(read_file())
    Words = []
    for i in data:
        word=i.strip()
        wordtypes = []
        meanings = []
        meaning=dictionary.meaning(word)
        if meaning is not None:
            for key in meaning.keys():
                wordtypes.append(key)
                meanings.append(meaning[key])
            Words.append(Word(word,wordtypes,meanings))
    return Words
                
Words=build_words()
for word in Words:
    print(word)

        
    

    
