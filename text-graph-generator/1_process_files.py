import os
import json

from func.input_to_list import *

input_files_folder = "input/"
output_files_folder = "output/1_process_files/"

input_files = os.listdir(input_files_folder)
output_files = os.listdir(output_files_folder)

for i in input_files:
    if i[-4:] == ".txt":
        if f"{i[:-4]}.json" not in output_files:
            print(f"Reading file: {i}")
            output_list = input_to_list(input_files_folder+i)
            with open(f"{output_files_folder}{i[:-4]}.json", "w") as result_file:
                json.dump({"list":output_list}, result_file)
            print(f"Output written to: {output_files_folder}{i[:-4]}.json")
        else:
            print(f"Skip file: {i}")

