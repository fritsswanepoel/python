def create_nodes_and_edges(input_list, unique_edge=False):
    edges_list = []
    progress_list = []
    ordered_edges_list = []
    node_count = {}

    #Create edge tuples
    for i in range(len(input_list)-1):
        if input_list[i] > input_list[i+1]:
            ordered_edge = f"{input_list[i]}_{input_list[i+1]}"
            edge_tuple = (input_list[i], input_list[i+1])
        else:
            ordered_edge = f"{input_list[i+1]}_{input_list[i]}"
            edge_tuple = (input_list[i+1], input_list[i])

        progress_list.append((input_list[i], input_list[i+1]))

        if unique_edge and ordered_edge not in ordered_edges_list:
            ordered_edges_list.append(ordered_edge)
            edges_list.append(edge_tuple)
        elif not unique_edge:
            edges_list.append(edge_tuple)

        if input_list[i] in node_count:
            node_count[input_list[i]]+=1
        else:
            node_count[input_list[i]]=1

        if i == len(input_list)-1:
            if input_list[i+1] in node_count:
                node_count[input_list[i+1]]+=1
            else:
                node_count[input_list[i+1]]=1



    print(f"Input list size: {len(input_list)}")
    print(f"Output nodes: {len(node_count)}")
    print(f"Output edges: {len(edges_list)}")
    print(f"Progress list: {len(progress_list)}")

    return edges_list, node_count, progress_list

