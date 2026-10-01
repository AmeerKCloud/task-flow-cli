import os

if os.path.exists("data.txt"):
    with open(file="data.txt") as f:
        contents = f.read()
        if contents.strip():
            print(contents)
        else:
            print("File is empty.")


