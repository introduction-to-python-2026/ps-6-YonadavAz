def create_codon_dict(file_path):
    path = {}
    # file = open(file_path)
    # rows = file.readlines()
    # file.close()
    with open( file_path) as file:
        rows = file.readlines()
    for row in rows:
        row.strip().split("/t")
        path = create_codon_dict(row)
    return path

if
