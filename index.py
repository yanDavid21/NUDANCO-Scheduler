import sys
from csv_parser import DanceSplitParser
from utils import convert_dict_to_graph_matrix, convert_hamilton_path_to_dance_names, get_complement_of_graph, get_hamilton_path_from_graph, partition_dict
import random
import os
import sys
from args_parser import ArgParser

MAX_ITERATION_ATTEMPTS = 100000


def main():
    parser = DanceSplitParser(ArgParser().get_file_name())
    dance_splits_dict, dance_splits_dict_keys = parser.as_dictionary(
        parser.dance_splits)

    for _ in range(MAX_ITERATION_ATTEMPTS):
        random.shuffle(dance_splits_dict_keys)
        dance_splits_dict_1, dance_splits_dict_2, dance_splits_dict_keys_1, dance_splits_dict_keys_2 = partition_dict(
            dance_splits_dict, dance_splits_dict_keys)

        graph_matrix_1 = get_complement_of_graph(
            convert_dict_to_graph_matrix(dance_splits_dict_1))
        path_1 = get_hamilton_path_from_graph(graph_matrix_1, [])

        graph_matrix_2 = get_complement_of_graph(
            convert_dict_to_graph_matrix(dance_splits_dict_2))
        path_2 = get_hamilton_path_from_graph(graph_matrix_2, [])

        if (path_1 and path_2):
            print(convert_hamilton_path_to_dance_names(
                path_1, dance_splits_dict_keys_1))
            print("Intermission")
            print(convert_hamilton_path_to_dance_names(
                path_2, dance_splits_dict_keys_2))
            sys.exit()


if __name__ == "__main__":
    main()
