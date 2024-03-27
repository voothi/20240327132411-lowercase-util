import argparse
import pyperclip

def to_lower_case(input_string):
    return input_string.lower()

def main():
    parser = argparse.ArgumentParser(description="Convert input string or clipboard content to lowercase.")
    parser.add_argument("input_string", nargs='?', type=str, help="Input string to convert to lowercase. If not provided, clipboard content will be used.")
    args = parser.parse_args()

    if args.input_string is None:
        clipboard_content = pyperclip.paste()
        output_string = to_lower_case(clipboard_content)
    else:
        output_string = to_lower_case(args.input_string)

    print(output_string)

if __name__ == "__main__":
    main()