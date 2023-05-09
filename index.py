from graph import DanceGraph
from utils import get_random_partition, parse_dance_source_file, process_and_print_result

MAX_ITERATION_ATTEMPTS = 100000


def main():
    dance_splits, dance_splits_keys = parse_dance_source_file()

    for _ in range(MAX_ITERATION_ATTEMPTS):
        partition_1, partition_2 = get_random_partition(
            dance_splits, dance_splits_keys)

        graph_matrix_1 = DanceGraph(
            dance_dict=partition_1.dict).get_complement()
        path_1 = graph_matrix_1.get_hamilton_path()

        graph_matrix_2 = DanceGraph(
            dance_dict=partition_2.dict).get_complement()
        path_2 = graph_matrix_2.get_hamilton_path()

        process_and_print_result(path_1, path_2, partition_1, partition_2)
    print("Could not find valid schedule, try again.")


if __name__ == "__main__":
    main()
