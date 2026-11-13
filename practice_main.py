import os

# if os.path.exists("test.txt"):
#     print("Exists")
# else:
#     print("Not exists.")


while True:
    with open(file="test.txt", mode="w") as f:
        f.write(input("Enter something:\n"))