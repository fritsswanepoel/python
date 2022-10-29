
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.collections import LineCollection

import networkx as nx
import json, os
import pickle as pl
import numpy as np
import pandas as pd

input_component_folder = "output/2_nodes_and_edges_files/"
input_graph_folder = "output/3_graphs/"
input_node_folder = "output/4_select_nodes/"

output_folder = "output/5_svg/"

edge_approach = 'unique'
figsize=(40,30)

plt.box(on=None)
plt.axis('off')

input_files = os.listdir(input_component_folder)

for input_file in input_files:
    print(input_file)
    order_color_list = []
    file_name = input_file[:-5]
    #Read in edges
    with open(f"{input_component_folder}{input_file}") as edge_list_file:
        if edge_approach == 'single':
            edges_list = json.load(edge_list_file)["progress_list"]
        else:
            edges_list = json.load(edge_list_file)["single_pass_list"]
    #Read in graph components
    with open(f"{input_graph_folder}{input_file[:-5]}_pos.pickle", 'rb') as pos_file:
        positions = pl.load(pos_file)

    with open(f"{input_graph_folder}{input_file[:-5]}_curves.pickle", 'rb') as curves_file:
        curves = pl.load(curves_file)

    with open(f"{input_graph_folder}{input_file[:-5]}_edges.pickle", 'rb') as edges_file:
        edges = pl.load(edges_file)

    g = nx.read_gpickle(f"{input_graph_folder}{input_file[:-5]}_g.pickle")

    #Read in node colors   
    focus_nodes = pd.read_csv(f"{input_node_folder}{input_file[:-5]}.csv")
    focus_nodes = focus_nodes.to_dict("list")

    try:
        os.mkdir(output_folder+file_name+edge_approach)
    except:
        pass
    output_files = os.listdir(output_folder+file_name+edge_approach)
    if f"{file_name}_total.png" in os.listdir(output_folder):
        print(f"Skip: {file_name}_total.png")
    else:
        plt.figure()
        # Base graph
        # Work out the line colors
        for e in edges:
            if len(set(focus_nodes['node']) & set(e)) > 0:
                for i in range(len(focus_nodes['node'])):
                    if focus_nodes['node'][i] in e:
                        order_color_list.append(to_rgba(focus_nodes['color'][i],1.0))
                        break

            else:
                order_color_list.append((0.0,0.0,0.0,0.05))


        # Create line collection
        lc = LineCollection(curves, color=order_color_list, linewidth=1)

        #Read in edge order
        plt.figure(figsize=figsize)

        nx.draw_networkx_nodes(g, positions, node_size=0.25, node_color='black', alpha=0.05)
        plt.gca().add_collection(lc)

        plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
        plt.savefig(f"{output_folder}/{file_name}_total.png", dpi=300, bbox_inches='tight')
        #plt.savefig(f"{output_folder}{file_name}/{file_name}_total.svg")

        plt.close("all")


    if f"{file_name}_total.svg" in os.listdir(output_folder):
        print(f"Skip: {file_name}_total.svg")
    else:
        plt.figure()
        # Base graph
        # Work out the line colors
        for e in edges:
            if len(set(focus_nodes['node']) & set(e)) > 0:
                for i in range(len(focus_nodes['node'])):
                    if focus_nodes['node'][i] in e:
                        order_color_list.append(to_rgba(focus_nodes['color'][i],1.0))
                        break

            else:
                order_color_list.append((0.0,0.0,0.0,0.05))


        # Create line collection
        lc = LineCollection(curves, color=order_color_list, linewidth=1)

        #Read in edge order
        plt.figure(figsize=figsize)

        nx.draw_networkx_nodes(g, positions, node_size=0.25, node_color='black', alpha=0.05)
        plt.gca().add_collection(lc)

        plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
        plt.savefig(f"{output_folder}/{file_name}_total.svg", bbox_inches='tight')
        #plt.savefig(f"{output_folder}{file_name}/{file_name}_total.svg")

        plt.close("all")



    # Animation
    for edge_number in range(len(edges_list)+4):
        if f"{file_name}_{edge_number}.png" in output_files:
            print(f"Skip: {file_name}_{edge_number}.png")
        else:
            plt.figure()
            order_color_list = []
            g = nx.read_gpickle(f"{input_graph_folder}{input_file[:-5]}_g.pickle")
            if edge_approach == 'single':
                try:
                    edge_list_1 = edges_list[edge_number]
                except:
                    edge_list_1 = []
                try:
                    edge_list_2 = edges_list[edge_number-1]
                except:
                    edge_list_2 = []
                try:
                    edge_list_3 = edges_list[edge_number-2]
                except:
                    edge_list_3 = []
                try:
                    edge_list_4 = edges_list[edge_number-3]
                except:
                    edge_list_4 = []
                try:
                    edge_list_5 = edges_list[edge_number-4]
                except:
                    edge_list_5 = []
            elif edge_approach == 'unique':
                try:
                    edge_list_1 = edges_list[edge_number]
                except:
                    edge_list_1 = [[]]
                try:
                    edge_list_2 = edges_list[edge_number-1]
                except:
                    edge_list_2 = [[]]
                try:
                    edge_list_3 = edges_list[edge_number-2]
                except:
                    edge_list_3 = [[]]
                try:
                    edge_list_4 = edges_list[edge_number-3]
                except:
                    edge_list_4 = [[]]
                try:
                    edge_list_5 = edges_list[edge_number-4]
                except:
                    edge_list_5 = [[]]
            print(f"{edge_number}/{len(edges_list)}: {len(edge_list_1)}")
            for e in edges:
                if len(set(focus_nodes['node']) & set(e)) > 0:
                    for i in range(len(focus_nodes['node'])):
                        if focus_nodes['node'][i] in e:
                            if edge_approach == 'single':
                                if len(set(edge_list_1) & set(e)) == 2:
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],1.0))
                                elif edge_number > 0 and len(set(edge_list_2) & set(e)) == 2:
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.8))
                                elif edge_number > 1 and len(set(edge_list_3) & set(e)) == 2:
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.6))
                                elif edge_number > 2 and len(set(edge_list_4) & set(e)) == 2:
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.4))
                                elif edge_number > 3 and len(set(edge_list_5) & set(e)) == 2:
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.2))
                                else:
                                    order_color_list.append((0.0,0.0,0.0,0.0))
                                break
                            elif edge_approach == 'unique':
                                if [e[0], e[1]] in edge_list_1 or [e[1], e[0]] in edge_list_1:
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],1.0))
                                elif edge_number > 0 and ([e[0], e[1]] in edge_list_2 or [e[1], e[0]] in edge_list_2):
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.8))
                                elif edge_number > 1 and ([e[0], e[1]] in edge_list_3 or [e[1], e[0]] in edge_list_3):
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.6))
                                elif edge_number > 2 and ([e[0], e[1]] in edge_list_4 or [e[1], e[0]] in edge_list_4):
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.4))
                                elif edge_number > 3 and ([e[0], e[1]] in edge_list_5 or [e[1], e[0]] in edge_list_5):
                                    order_color_list.append(to_rgba(focus_nodes['color'][i],0.2))
                                else:
                                    order_color_list.append((0.0,0.0,0.0,0.0))
                                break

                else:
                    if edge_approach == 'single':
                        if len(set(edge_list_1) & set(e)) == 2:
                            order_color_list.append(to_rgba('black',0.5))
                        elif edge_number > 0 and len(set(edge_list_2) & set(e)) == 2:
                            order_color_list.append(to_rgba('black',0.4))
                        elif edge_number > 1 and len(set(edge_list_3) & set(e)) == 2:
                            order_color_list.append(to_rgba('black',0.3))
                        elif edge_number > 2 and len(set(edge_list_4) & set(e)) == 2:
                            order_color_list.append(to_rgba('black',0.2))
                        elif edge_number > 3 and len(set(edge_list_5) & set(e)) == 2:
                            order_color_list.append(to_rgba('black',0.1))
                        else:
                            order_color_list.append(to_rgba('black',0.0))
                    elif edge_approach == 'unique':
                        if [e[0], e[1]] in edge_list_1 or [e[1], e[0]] in edge_list_1:
                            order_color_list.append(to_rgba('black',0.3))
                        elif edge_number > 0 and ([e[0], e[1]] in edge_list_2 or [e[1], e[0]] in edge_list_2):
                            order_color_list.append(to_rgba('black',0.2))
                        elif edge_number > 1 and ([e[0], e[1]] in edge_list_3 or [e[1], e[0]] in edge_list_3):
                            order_color_list.append(to_rgba('black',0.15))
                        elif edge_number > 2 and ([e[0], e[1]] in edge_list_4 or [e[1], e[0]] in edge_list_4):
                            order_color_list.append(to_rgba('black',0.1))
                        elif edge_number > 3 and ([e[0], e[1]] in edge_list_5 or [e[1], e[0]] in edge_list_5):
                            order_color_list.append(to_rgba('black',0.05))
                        else:
                            order_color_list.append(to_rgba('black',0.0))

            # Create line collection
            lc = LineCollection(curves, color=order_color_list, linewidth=3)

            #Read in edge order
            plt.figure(figsize=figsize)

            nx.draw_networkx_nodes(g, positions, node_size=0.25, node_color='black', alpha=0.01)
            plt.gca().add_collection(lc)

            plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
            plt.savefig(f"{output_folder}{file_name}{edge_approach}/{file_name}_{edge_number}.png", dpi=300, bbox_inches='tight')
            #plt.savefig(f"{output_folder}{file_name}_{edge_number}.svg")
            plt.close("all")
