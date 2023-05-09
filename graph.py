import numpy
from utils import has_dancers_in_both_dances
import copy


class DanceGraph:
    def __init__(self, dance_dict=None, graph_matrix=None) -> None:
        if graph_matrix is None:
            index_to_dance_map = list(dance_dict.keys())
            self.graph_matrix = numpy.zeros(
                [len(index_to_dance_map), len(index_to_dance_map)], dtype=int)
            for dance1 in range(0, len(index_to_dance_map)):
                for dance2 in range(0, len(index_to_dance_map)):
                    is_overlapping = dance1 == dance2 or has_dancers_in_both_dances(
                        dance1, dance2, index_to_dance_map, dance_dict)
                    self.graph_matrix[dance1][dance2] = is_overlapping
        else:
            self.graph_matrix = graph_matrix

    def get_complement(self):
        complement_graph_matrix = numpy.zeros(
            [len(self.graph_matrix), len(self.graph_matrix)], dtype=int)
        for i in range(len(self.graph_matrix)):
            for j in range(len(self.graph_matrix[0])):
                complement_graph_matrix[i][j] = 1 if self.graph_matrix[i][j] == 0 else 0
        return DanceGraph(graph_matrix=complement_graph_matrix)

    def get_hamilton_path(self, seen_before=[], starting_node=0):
        seen_before = copy.copy(seen_before) + [starting_node]
        if len(seen_before) == len(self.graph_matrix):
            return seen_before
        if starting_node == 0:
            for rowIdx in range(len(self.graph_matrix)):
                for colIdx in range(len(self.graph_matrix[rowIdx])):
                    if self.graph_matrix[rowIdx][colIdx] == 1 and colIdx not in seen_before:
                        return self.get_hamilton_path(seen_before, colIdx)
        else:
            for colIdx in range(len(self.graph_matrix[starting_node])):
                if self.graph_matrix[starting_node][colIdx] == 1 and colIdx not in seen_before:
                    return self.get_hamilton_path(seen_before, colIdx)
