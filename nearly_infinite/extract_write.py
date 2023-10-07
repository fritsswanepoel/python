
import random
import copy
from suffix_trees import STree
import json
import pandas as pd
from unidecode import unidecode
import re

#Read in file
input_files = [
    "collection/romeo_and_juliet.txt", 
    "collection/alices_adventures_in_wonderland.txt", 
    "collection/pride_and_prejudice.txt",
    "collection/the_adventures_of_sherlock_holmes.txt",
    ]


singles_freq = {}
pairs_freq = {}
triples_freq = {}

# start_char_pos = {}
char_pos = {}

for input_file in input_files:
    print(input_file)
    with open(input_file, 'r', encoding='utf-8') as f:
        file = f.read()

    # char_counter = 0
    # for c in file:
    #     if c not in char_pos:
    #         char_pos[c] = [0 for i in range(100)]

    #     pos = int(char_counter / len(file)*100)
    #     char_pos[c][pos] += 1

    #     char_counter += 1
        
    #Remove newlines
    file = ' '.join(file.splitlines())

    #Unidecode
    file = unidecode(file)

    #Simplify chars
    # file = re.sub('[^0-9a-zA-Z ,\.\'\-]','', file)

    #Remove multiple spaces
    file = re.sub(' +',' ', file)

    singles = file.split(' ')

    # term_pos = 0
    for i in range(len(singles)):
        if singles[i] in singles_freq:
            singles_freq[singles[i]]['freq'] += 1
        else:
            singles_freq[singles[i]] = {'freq': 1}

    #     if len(singles[i]) > 0:
    #         first_char = singles[i][0].lower()
    #         if first_char not in start_char_pos:
    #             start_char_pos[first_char] = [0 for i in range(100)]

    #     pos = int(term_pos / len(singles)*100)
    #     start_char_pos[first_char][pos] += 1

    #     term_pos += 1

    for i in range(len(singles)-1):
        pair = f"{singles[i]} {singles[i+1]}"
        if pair in pairs_freq:
            pairs_freq[pair] += 1
        else:
            pairs_freq[pair] = 1

    for i in range(len(singles)-2):
        triple = f"{singles[i]} {singles[i+1]} {singles[i+2]}"
        if triple in triples_freq:
            triples_freq[triple] += 1
        else:
            triples_freq[triple] = 1


words = 1000
story = ""

start = random.choice(singles)
start_prev = ' '

story += start

stats = {}

stats["words"] = words
stats["single"] = 0
stats["pairs"] = 0
stats["triples"] = 0

print("generating")
while words > 0:
    #Possible word pairs
    possible = []
    possible_freq = []
    for key, value in triples_freq.items():
        if ' '.join(key.split(' ')[:-1]) == f"{start_prev} {start}":
            possible.append(key)
            possible_freq.append(value)
    if len(possible_freq) <= 1:
        possible = []
        possible_freq = []
        for key, value in pairs_freq.items():
            if key.split(' ')[0] == start:
                possible.append(key)
                possible_freq.append(value)
    else:
        stats["triples"] += 1
    #If nothing good, use single
    if len(possible) <=1:
        for key, value in singles_freq.items():
            possible.append(key)
            possible_freq.append(value)
        stats["single"] += 1
    else:
        stats["pairs"] += 1
    #Pick work
    selected = random.choices(possible, k=1, weights=possible_freq)[0]
    start_prev = copy.deepcopy(start)
    start = selected.split(' ')[-1]
    story += f' {start}'
    words -= 1


with open('story.txt','w') as f:
    f.write(story)

#stats["story"] = story
stats["input"] = input_files

# a = [file, story]
# st = STree.STree(a)

# stats["longest_common_string"] = st.lcs()

story
print(stats)

# with open("sample.json", "w", encoding='utf-8') as outfile:
#     json.dump(start_char_pos, outfile)

# df = pd.DataFrame(start_char_pos)
# df.to_csv('single_count.csv', index=False)

# df = pd.DataFrame(char_pos)
# df.to_csv('char_count.csv', index=False)