with open("cal", "rb") as f:
    while b := f.read(1):
        print(f"{b[0]:08b}")
    print()

