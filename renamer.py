

from os import walk, rename
from re import search


def add_difficulty(difficulty: str, filename: str):
    """
    Renames the file and adds the difficalty after the problem's
    number.

    111-some-problem.py -> 111-easy-some-problem.py

    Assumes the file name follows the following format:

    NUMBER-some-problem-name.py
    """

    problem_number = filename.split("-")[0]
    problem_name = "-".join(filename.split("-")[1:])

    print(f"Renaming: {filename}")

    new_filename = "-".join([problem_number, difficulty, problem_name])
    rename(filename, new_filename)
    #print(f"Dry run:\n\t{filename} -> {new_filename}")


def main():
    filename_pattern = r"^[0-9]+.+\.py$"

    for _, _, files in walk("."):
        for file in files:
            if search(filename_pattern, file):
                add_difficulty("easy", file)


main()

