import os

# if os.path.exists("test.txt"):
#     print("Exists")
# else:
#     print("Not exists.")


while True:
    with open(file="test.txt", mode="w") as f:
        f.write(input("Enter something:\n"))

    keep_going = input("Continue? Y/N?\n")

    if keep_going == "n":
        with open(file="test.txt", mode="w") as f:
            pass
        break