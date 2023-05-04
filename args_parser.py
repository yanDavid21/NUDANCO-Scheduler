import argparse
import os


class ArgParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog='NUDanco Scheduler',
            description='What the program does',
            epilog='Text at the bottom of help')  # TODO
        self.parser.add_argument('filename')

    def get_file_name(self) -> str:
        args = self.parser.parse_args()

        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_name = os.path.join(file_dir, args.filename)
        return file_name
