def create_codon_dict(file_path):
    path = {}
    # file = open(file_path)
    # rows = file.readlines()
    # file.close()
    with open(file_path) as file:
        rows = file.readlines()
    for row in rows:
        row.strip().split("/t")
        path = create_codon_dict(row)
    return path

if __name__ == "__main__":
    result = create_codon_dict("data/codons.txt")

    assert result['AAA'] == 'K', "Test Failed: 'AAA' should map to 'K'"
    assert result['AAC'] == 'N', "Test Failed: 'AAC' should map to 'N'"

    assert result['ACA'] == 'T', "Test Failed: 'ACA' should map to 'T'"
    assert result['ACC'] == 'T', "Test Failed: 'ACC' should map to 'T'"

    print("All tests passed successfully.")

