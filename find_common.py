from fuzzywuzzy import process
from nltk.stem.snowball import RussianStemmer
l = ['банан', 'яйца', 'мука', 'картофель']
stemmer  = RussianStemmer()
stem_l = [stemmer.stem(x) for x in l]  # ['бана', 'яйц', 'мук', 'картофел']
ingredient = stemmer.stem("картошка")  # 'картошк'
print(process.extractOne(ingredient, stem_l))  # ('картофел', 67)




# from difflib import SequenceMatcher
# from itertools import combinations, imap

# def ratio(pair):
#     return (SequenceMatcher(None, *pair).ratio(), pair[0])

# def findword(wordlist):
#     pairs = combinations(wordlist, 2)
#     found = max(imap(ratio, pairs))[1] 
#     return found

# print findword('голубец', 'конь', 'голубцы', 'лист')
# print findword(['стол', 'день', 'свет', 'клинок', 'светильник'])
# print findword(['восток', 'дань', 'исток', 'жир', 'голубь', 'да'])