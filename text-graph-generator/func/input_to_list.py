
import unidecode
import re


def input_to_list(file_name, edge_cap=None, upper_case=True, apply_unidecode=True, remove_punctuation=True):
    start_delimiter = ""
    end_delimiter = ""
    #Split out the individual words
    re_multi = re.compile(r"\s+")

    result = []
    counter = 0
    started = False
    with open(f'{file_name}',encoding='UTF8') as f:
        for line in f:
            if re.match(end_delimiter,  line):
                break
            elif started:
                result_initial = []
                counter += 1
                if upper_case:
                    line = line.upper()
                if apply_unidecode:
                    line = unidecode.unidecode(line)
                if remove_punctuation:
                    line = re_multi.sub(" ",re.sub("[^0-9A-Z ]","",line))
                inner_list = line.split(' ')
                if len(inner_list) == 1 and inner_list[0] == '':
                    pass
                else:
                    for r in inner_list:
                        if r not in ('',' '):
                            result_initial.append(r)
                    result.extend(result_initial)
                if edge_cap:
                    if len(result) >= edge_cap:
                        break
            elif re.match(start_delimiter, line):
                started = True
    
    if result == []:
        with open(f'{file_name}',encoding='UTF8') as f:
            for line in f:
                result_initial = []
                counter += 1
                if upper_case:
                    line = line.upper()
                if apply_unidecode:
                    line = unidecode.unidecode(line)
                if remove_punctuation:
                    line = re_multi.sub(" ",re.sub("[^0-9A-Z ]","",line))
                inner_list = line.split(' ')
                if len(inner_list) == 1 and inner_list[0] == '':
                    pass
                else:
                    for r in inner_list:
                        if r not in ('',' '):
                            result_initial.append(r)
                    result.extend(result_initial)
                if edge_cap:
                    if len(result) >= edge_cap:
                        break


    print(f"Extracted {len(result)} items from {file_name}")
    return result
