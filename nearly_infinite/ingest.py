

import os, re, json

from unidecode import unidecode

#Load corpus
corpus_file = 'data/corpus.json'
collection_dir = 'collection'

max_terms = 3

if os.path.isfile(corpus_file):
    with open(corpus_file,'r',encoding="utf-8") as f:
        corpus = json.load(f)

    print(corpus['len'].keys())
else:
    corpus = {
        "collection":{},
        "len":{
            '1':{},
            '2':{},
            '3':{},
            '4':{},
            '5':{}
            },
        "terms":{}
        }

#Check for new files
if os.path.exists(collection_dir):
    collections = [f"{collection_dir}/{f}" for f in os.listdir(collection_dir) if f"{collection_dir}/{f}" not in corpus["collection"] and ".txt" in f]
else:
    os.mkdir(collection_dir)
    collections = []

print(corpus["collection"].keys())
#Process each file and add to corpus
for collection in collections:

    print(collection)
    with open(collection, 'r', encoding='utf-8') as f:
        file = f.read()

    #Remove newlines
    file = ' '.join(file.splitlines())

    #Unidecode
    file = unidecode(file)

    #Remove multiple spaces
    file = re.sub(' +',' ', file)

    singles = file.split(' ')

    #Add single terms with counts
    for s in singles:
        if s in corpus["terms"]:
            corpus["terms"][s] += 1
        else:
            corpus["terms"][s] = 1

    total_count = len(singles)

    for pos in range(0, total_count):
        term = ''
        for t in range(0, max_terms):
            if pos + t < total_count:
                term = term + ' ' + singles[pos + t]
                term = term.strip()

                if term not in corpus["len"][str(t+1)]:
                    corpus["len"][str(t+1)][term] = {}
                    corpus["len"][str(t+1)][term]["occs"] = 1
                    corpus["len"][str(t+1)][term]["following"] = {}
                    corpus["len"][str(t+1)][term]["number_following"] = 0

                corpus["len"][str(t+1)][term]["occs"] += 1
                if pos + t < total_count - 1:
                    if singles[pos + t + 1] in corpus["len"][str(t+1)][term]["following"]:
                        corpus["len"][str(t+1)][term]["following"][singles[pos + t + 1]] += 1
                    else:
                        corpus["len"][str(t+1)][term]["following"][singles[pos + t + 1]] = 1
                        corpus["len"][str(t+1)][term]["number_following"] += 1
            

    corpus["collection"][collection] = {
        "words":len(singles),
        "unique_words":len(set(singles))
        }

    #Write out corpus
    with open(corpus_file, 'w', encoding="utf-8") as f:
        json.dump(corpus,f)

print(corpus["collection"])