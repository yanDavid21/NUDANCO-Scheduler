from math import floor
import random
from args_parser import ArgParser
from csv_parser import DanceSplitParser
import sys


class OrderedDict:
    def __init__(self, dict, keys) -> None:
        self.dict = dict
        self.keys = keys


def parse_dance_source_file():
    parser = DanceSplitParser(ArgParser().get_file_name())
    dance_splits, dance_splits_keys = parser.as_dictionary(
        parser.dance_splits)
    return dance_splits, dance_splits_keys


def has_dancers_in_both_dances(dance1_index, dance2_index, index_to_dance_map, dance_dict):
    dance1 = index_to_dance_map[dance1_index]
    dance2 = index_to_dance_map[dance2_index]
    dancers_in_dance1 = dance_dict.get(dance1)
    dancers_in_dance2 = dance_dict.get(dance2)
    intersection = dancers_in_dance1.intersection(dancers_in_dance2)
    return len(intersection) != 0


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
    return OrderedDict(partition_dict_1,
                       dance_splits_dict_keys_1), OrderedDict(partition_dict_2,
                                                              dance_splits_dict_keys_2)


def get_random_partition(dance_splits_dict, dance_splits_dict_keys):
    random.shuffle(dance_splits_dict_keys)
    partition_1, partition_2 = partition_dict(
        dance_splits_dict, dance_splits_dict_keys)
    return partition_1,  partition_2


def process_and_print_result(path_1, path_2, partition_1, partition_2):
    if (path_1 and path_2):
        print(convert_hamilton_path_to_dance_names(
            path_1, partition_1.keys))
        print("Intermission")
        print(convert_hamilton_path_to_dance_names(
            path_2, partition_2.keys))
        sys.exit()
