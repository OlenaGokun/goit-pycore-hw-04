def total_salary(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    totalSalary = 0
    workersCount = 0
    for line in lines:
        workerData = line.split(",")
        try:
            salary = int(workerData[1])
        except (IndexError, ValueError):
            print("Input file is corrupted. Skipping the record")
        else:
            totalSalary += salary
            workersCount += 1

    return (totalSalary, totalSalary / workersCount if workersCount != 0 else 0)