class WordsFinder:

    def __init__(self,*file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name,encoding='utf-8') as file:
                file = file.read()
                file = file.lower()
                file = file.replace(' - ',' ')
                punkt = [',','.','=','!','?',';',':']
                for p in punkt:
                    if p in file:
                        file = file.replace(p,'')
                all_words[file_name] = file.split()
        return all_words

    def find(self,word):
        find_words = {}
        for key,value in self.get_all_words().items():
            if word.lower() in value:
                find_words[key] = value.index(word.lower()) + 1
        return find_words

    def count(self,word):
        count_words = {}
        for key,value in self.get_all_words().items():
            if word.lower() in value:
                count_words[key] = value.count(word.lower())
        return count_words


finder2 = WordsFinder('test_file.txt','test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('if')) # 4 слова teXT в тексте всего