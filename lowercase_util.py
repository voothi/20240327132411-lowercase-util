import argparse

def to_lower_case(input_string):
    return input_string.lower()

def main():
    parser = argparse.ArgumentParser(description="Convert input string to lowercase.")
    parser.add_argument("input_string", type=str, help="Input string to convert to lowercase.")
    args = parser.parse_args()

    output_string = to_lower_case(args.input_string)
    print(output_string)

if __name__ == "__main__":
    main()