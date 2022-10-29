
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

import networkx as nx
import json, os
import pickle as pl

from fa2 import ForceAtlas2

from func.curved_edges import curved_edges

# Variables
node_iter = 1000
polarity = 'alternate' # 'fixed', 'alternate', 'other'

input_files_folder = "output/2_nodes_and_edges_files/"
output_files_folder = "output/3_graphs/"

input_files = os.listdir(input_files_folder)
output_files = os.listdir(output_files_folder)

for i in input_files:
    if i[-5:] == ".json":
        if f"{i[:-5]}_curves.pickle" not in output_files or f"{i[:-5]}_edges.pickle" not in output_files or f"{i[:-5]}_pos.pickle" not in output_files or f"{i[:-5]}_g.pickle" not in output_files:
            print(f"Reading file: {i}")
            with open(f"{input_files_folder}{i}") as input_file:
                edges_list = json.load(input_file)["edges_list"]

            # Create graph
            g = nx.MultiGraph()

            # Add edges
            g.add_edges_from(edges_list)

            # Calculate node positions
            forceatlas2 = ForceAtlas2(
                                    # Behavior alternatives
                                    outboundAttractionDistribution=True,  # Dissuade hubs
                                    edgeWeightInfluence=1.0,
                                    # Tuning
                                    scalingRatio=5.0, #2.0
                                    strongGravityMode=False,
                                    gravity=0.5) # 1.0

            positions = forceatlas2.forceatlas2_networkx_layout(g, pos=None, iterations=node_iter)

            # Produce the curves
            curves, edges = curved_edges(g, positions, polarity=polarity)

            # Write out pickle files
            with open(f'{output_files_folder}{i[:-5]}_pos.pickle', 'wb') as output_file:
                pl.dump(positions, output_file) 

            with open(f'{output_files_folder}{i[:-5]}_curves.pickle', 'wb') as output_file:
                pl.dump(curves, output_file) 

            with open(f'{output_files_folder}{i[:-5]}_edges.pickle', 'wb') as output_file:
                pl.dump(edges, output_file) 

            with open(f'{output_files_folder}{i[:-5]}_g.pickle', 'wb') as output_file:
                nx.write_gpickle(g, output_file)
                
            print(f"Output written to: {output_files_folder}{i[:-5]}_pos.pickle")
            print(f"Output written to: {output_files_folder}{i[:-5]}_curves.pickle")
            print(f"Output written to: {output_files_folder}{i[:-5]}_edges.pickle")
            print(f"Output written to: {output_files_folder}{i[:-5]}_g.pickle")
        else:
            print(f"Skip file: {i}")