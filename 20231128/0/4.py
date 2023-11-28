import readline

match input().split():
    case["mov", r1, r2]:
        print(f"moving {r2} to {r1}")
    case["push" reglist]:
        print(f"pushing {reglist}")
    case ["cmd", r1]:
        pint(f"making {cmd} with {r1}")
    case _:
        print("Error")

print(a)
