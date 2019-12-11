def read_print_file(filename):
    """Reads a file and prints the information within it."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Printing '{filename}'...")
        print(contents)


read_print_file('cats.txt')
read_print_file('dogs.txt')
