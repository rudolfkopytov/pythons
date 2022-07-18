def save(data, FILENAME):
    for rec in data:
        rec[2] = str(rec[2])
    with open(FILENAME, "w") as f:
        json.dump(data, f)


def read(FILENAME):
    if os.path.isfile(FILENAME):
        with open(FILENAME) as f:
            data = json.load(f)
    else:
        data = []

    for rec in data:
        date_ints = map(int, rec[2].split("-"))
        rec[2] = dt.date(*date_ints)

    return data