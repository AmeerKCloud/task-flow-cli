list_1 = ["one", "two", "three", "two"]

occurance = 0

for item in list_1:
    print(item)
    for item in list_1:
        if item == item:

        print(f"Inner loop: {item}")

