import os
import os.path
import sys
def search_path(path, text):
    for x in os.listdir(path):
        if os.path.isdir(x):
            search_path(os.path.join(path, x), text)
        elif x.strip().find(text) != -1:
            print os.path.join(path, x)


if __name__ == '__main__':
    search_path('.', sys.argv[1])