
import pandas as pd
import os, random, json


input_files_folder = "output/2_nodes_and_edges_files/"
output_files_folder = "output/4_select_nodes/"

input_files = os.listdir(input_files_folder)
output_files = os.listdir(output_files_folder)

color_list = ['firebrick',
    'seagreen',
    'royalblue',
    'gold',
    'darkorange',
    'darkmagenta'
    ]


for i in input_files:
    if i[-5:] == ".json":
        if f"{i[:-5]}.csv" not in output_files:
            focus_nodes = []
            color_count = 3
            print(f"Reading file: {i}")
            with open(f"{input_files_folder}{i}") as input_file:
                focus_node_color_list = random.sample(color_list, color_count)

                node_count = json.load(input_file)["node_count"]

                if len(node_count) < color_count:
                    color_count = len(node_count)

                if color_count > 0:

                    # Pick nodes to individually color
                    df = pd.DataFrame.from_dict(node_count, orient='index')
                    df = df.sort_values(by=[0], ascending=False)

                    df['cumsum'] = df[[0]].cumsum()

                    df = df[df['cumsum'] <= 0.3*df[['cumsum']].max().iloc[0]]
                    color_count = min(color_count, df.shape[0])
                    df = df.sample(color_count)
                    df.reset_index(level=0, inplace=True)

                    for c in range(color_count):
                        focus_nodes.append({
                            "node":df.iloc[c]['index'],
                            "count":df.iloc[c][0],
                            "color":focus_node_color_list[c],
                            "position":c
                        })

                    df = pd.DataFrame(focus_nodes)
                    df.to_csv(f"{output_files_folder}{i[:-5]}.csv",index=False)
                
                    print(f"Output written to: {output_files_folder}{i[:-5]}.csv")
        else:
            print(f"Skip file: {i}")
