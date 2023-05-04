from math import floor
import numpy
import copy


def convert_dict_to_graph_matrix(dance_dict):
    index_to_dance_map = list(dance_dict.keys())
    graph_matrix = numpy.zeros(
        [len(index_to_dance_map), len(index_to_dance_map)], dtype=int)
    for dance1 in range(0, len(index_to_dance_map)):
        for dance2 in range(0, len(index_to_dance_map)):
            if dance1 == dance2 or has_dancers_in_both_dances(dance1, dance2, index_to_dance_map, dance_dict):
                graph_matrix[dance1][dance2] = 1
            else:
                graph_matrix[dance1][dance2] = 0
    return graph_matrix


def has_dancers_in_both_dances(dance1_index, dance2_index, index_to_dance_map, dance_dict):
    dance1 = index_to_dance_map[dance1_index]
    dance2 = index_to_dance_map[dance2_index]
    dancers_in_dance1 = dance_dict.get(dance1)
    dancers_in_dance2 = dance_dict.get(dance2)
    intersection = dancers_in_dance1.intersection(dancers_in_dance2)
    return len(intersection) != 0


def get_complement_of_graph(graph_matrix):
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[0])):
            graph_matrix[i][j] = 1 if graph_matrix[i][j] == 0 else 0
    return graph_matrix


def get_hamilton_path_from_graph(graph_matrix, seen_before, starting_node=0):
    seen_before = copy.copy(seen_before) + [starting_node]
    if len(seen_before) == len(graph_matrix):
        return seen_before
    if starting_node == 0:
        for rowIdx in range(len(graph_matrix)):
            for colIdx in range(len(graph_matrix[rowIdx])):
                if graph_matrix[rowIdx][colIdx] == 1 and colIdx not in seen_before:

                    return get_hamilton_path_from_graph(
                        graph_matrix, seen_before, colIdx)
    else:
        for colIdx in range(len(graph_matrix[starting_node])):
            if graph_matrix[starting_node][colIdx] == 1 and colIdx not in seen_before:
                return get_hamilton_path_from_graph(graph_matrix, seen_before, colIdx)


def convert_hamilton_path_to_dance_names(path, dance_split_dict_keys):
    dance_names = []
    for idx in path:
        dance_names.append(dance_split_dict_keys[idx])
    return dance_names


def partition_dict(dance_splits_dict, dance_splits_dict_keys):
    partition_key_idx = floor(len(dance_splits_dict_keys)/2)
    dance_splits_dict_keys_1 = dance_splits_dict_keys[0:partition_key_idx]
    dance_splits_dict_keys_2 = dance_splits_dict_keys[partition_key_idx:]
    partition_dict_1 = {}
    partition_dict_2 = {}
    # TODO: add list comprehension
    for idx in range(partition_key_idx):
        key = dance_splits_dict_keys[idx]
        partition_dict_1[key] = dance_splits_dict[key]
    for idx in range(partition_key_idx, len(dance_splits_dict_keys)):
        key = dance_splits_dict_keys[idx]
        partition_dict_2[key] = dance_splits_dict[key]
    return partition_dict_1, partition_dict_2, dance_splits_dict_keys_1, dance_splits_dict_keys_2
