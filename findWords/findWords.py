import sys
import os
import re

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wordsFile.txt")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No words provided")

    try:
        file = open(FILE_NAME, "r", encoding="utf8")
    except IOError:
        sys.exit("File does not exist")

    words_dict = {arg: 0 for arg in sys.argv[1:] if re.match(r"\w+", arg) is not None}

    find_re = re.compile(r"\b\w+\b")
    for line in file:
        for word in find_re.findall(line):
            if word in words_dict.keys():
                words_dict[word] += 1
    file.close()
    print("\n".join([f"{key}: {value}" for key, value in words_dict.items()]))