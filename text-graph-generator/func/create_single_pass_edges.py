def create_single_pass_edges(progress_list):
    single_pass_dict = {}
    single_pass_edge_list = []
    counter = 0

    for edge in progress_list:
        edge_string = f"{edge[0]}_{edge[1]}"
        edges = []
        counter2 = counter
        if edge_string not in single_pass_edge_list:
            single_pass_edge_list.append(edge_string)
            for next_edge in progress_list[counter:]:
                if edge == next_edge and counter2+1 < len(progress_list) and next_edge not in edges:
                    edges.append(progress_list[counter2+1])
                counter2+=1
            single_pass_dict[edge_string] = edges

        counter += 1
        if counter %10000 == 0:
            print(counter, len(single_pass_dict))

    print(f"Single pass dict of lists: {len(single_pass_dict)}")

    next_edge = [progress_list[0]]
    single_pass_edge_lists = [next_edge]
    used_edges = [progress_list[0]]

    counter = 0

    while len(next_edge) > 0:
        edge_list = []
        unique_edge_list = []
        for edge in next_edge:
            edge_list.extend(single_pass_dict[f"{edge[0]}_{edge[1]}"])

        for edge in edge_list:
            if edge not in unique_edge_list:
                if edge not in used_edges:
                    unique_edge_list.append(edge)
                    used_edges.append(edge)

        single_pass_edge_lists.append(unique_edge_list)
        next_edge = unique_edge_list
        counter+=1
        if counter %1000 == 0:
            print(counter, len(unique_edge_list), len(used_edges))

    print(f"Single pass list of lists: {len(single_pass_edge_lists)}")
    
    return single_pass_edge_lists