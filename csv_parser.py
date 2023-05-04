import csv


class DanceSplitParser:

    def __init__(self, filepath) -> None:
        self.dance_splits = []
        column_headers, csv_rows = self.parse(filepath)
        self.dance_splits = self.get_dance_splits(column_headers, csv_rows)

    # reading csv file
    def parse(self, filepath):
        csv_rows = []
        with open(filepath, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            column_headers = next(csvreader)
            for row in csvreader:
                csv_rows.append(row)
        return column_headers, csv_rows

    def get_dance_splits(self, column_headers, csv_rows):
        dance_splits = []
        for index in range(0, len(column_headers)):
            dance_name = column_headers[index]
            dance_splits += [[dance_name] +
                             self.get_dancers_of_a_dance(index, csv_rows)]
        return dance_splits

    def get_dancers_of_a_dance(self, dance_index, csv_rows):
        dancers = map(lambda row: row[dance_index], csv_rows)
        cleaned_dancers = filter(lambda dancer: dancer != "", dancers)
        return list(cleaned_dancers)

    def as_dictionary(self, dance_splits_arr):
        dance_split_dict = dict()
        for dance_split in dance_splits_arr:
            dance_name = dance_split[0]
            dancers = dance_split[1:]
            dance_split_dict[dance_name] = set(dancers)
        return dance_split_dict, list(dance_split_dict.keys())

    def print_dancers(self):
        print(self.dance_splits)
