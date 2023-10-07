
import random
import json
import copy
import os
from datetime import datetime

words = 1000
story = ""

corpus_file = 'data/corpus.json'

story_folder = 'story/'

stats = {
    "words": words,
    "unique_words":0,
    "0": 1,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0
    }

current_date = datetime.now().strftime("%Y%m%d")

if os.path.isfile(f"{story_folder}story_{current_date}.txt"):
    print(f"Story already exists for {current_date}")
else:

    with open(corpus_file,'r',encoding="utf-8") as f:
        corpus = json.load(f)

    start = random.choices([k for k in corpus["terms"].keys()], k=1, weights=[v for v in corpus["terms"].values()])[0]
    words -= 1
    # possible = []
    # occs = []
    # for k in corpus["len"]["3"].keys():
    #     print(k)
    #     possible.append(k)
    #     occs.append(corpus["len"]["3"][k]["occs"])
    # start = random.choices(possible, k=1, weights=occs)[0]
    start_prev = copy.deepcopy(start)

    story += start


    print("generating")
    selected = None

    while words > 0:
        start_len = len(start_prev.split(' '))
        if start_len > 3:
            start = ' '.join(start_prev.split(' ')[-3:])
            start_len = 3
        else:
            start = copy.deepcopy(start_prev)
        for i in range(start_len, 0, -1):
            start = ' '.join(start.split(' ')[-1*i:])
            if start in corpus["len"].get(str(i),[]):
                if len([k for k in corpus["len"][str(i)][start]["following"]]) > 3:
                    #Pick work
                    selected = random.choices([k for k in corpus["len"][str(i)][start]["following"].keys()], k=1, weights=[v for v in corpus["len"][str(i)][start]["following"].values()])[0]
                    stats[str(i)] += 1
                    break

        if not selected:
            selected = random.choices([k for k in corpus["terms"].keys()], k=1, weights=[v for v in corpus["terms"].values()])[0]
            stats["0"] += 1

        start_prev = start_prev + ' ' + selected
        story += f' {selected}'
        words -= 1
        selected = None

    unique_words = len(set(story.split(" ")))
    stats["unique_words"] = unique_words

    with open(f'{story_folder}story_{current_date}.txt','w',encoding='utf-8') as f:
        f.write(story)

    with open(f'{story_folder}story_stats_{current_date}.json','w',encoding='utf-8') as f:
        json.dump(stats, f)