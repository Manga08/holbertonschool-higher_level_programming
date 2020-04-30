#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for sort in dir(hidden_4):
        if not sort.startswith("__"):
            print("{}".format(sort))
