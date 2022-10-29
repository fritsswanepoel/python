import os
import json

from func.create_nodes_and_edges import *
from func.create_single_pass_edges import *

input_files_folder = "output/1_process_files/"
output_files_folder = "output/2_nodes_and_edges_files/"

unique_edge = True

input_files = os.listdir(input_files_folder)
output_files = os.listdir(output_files_folder)

for i in input_files:
    if i[-5:] == ".json":
        if i not in output_files:
            print(f"Reading file: {i}")
            with open(f"{input_files_folder}{i}") as input_file:
                input_list = json.load(input_file)["list"]

            edges_list, node_count, progress_list = create_nodes_and_edges(input_list, unique_edge)
            single_pass_list = create_single_pass_edges(progress_list)
            with open(f"{output_files_folder}{i}", "w") as result_file:
                json.dump({"edges_list":edges_list, "node_count":node_count, "progress_list":progress_list, "single_pass_list":single_pass_list}, result_file)
            print(f"Output written to: {output_files_folder}{i}")
        else:
            print(f"Skip file: {i}")
