def get_cats_info(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    cats = []
    for line in lines:
        catData = line.split(",")
        if len(catData) != 3:
            print("Corrupted data in file. Skipping the record")
            continue

        try:
            cat = [catData[0], catData[1], int(catData[2])]
        except ValueError:
            print("Corrupted data in file. Skipping the record")
            continue

        cats.append(dict(zip(["id", "name", "age"], cat)))
        
    return cats