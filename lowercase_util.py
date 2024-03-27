import argparse
import pyperclip
import re

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)

def to_lower_case(input_string):
    return input_string.lower()

def clean_text(input_string):
    # Удаляем HTML теги и другие скрытые символы
    clean_string = re.sub('<[^<]+?>', '', input_string)
    clean_string = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', clean_string)
    return clean_string

def main():
    parser = argparse.ArgumentParser(description="Convert input string or clipboard content to lowercase.")
    parser.add_argument("input_string", nargs='?', type=str, help="Input string to convert to lowercase. If not provided, clipboard content will be used.")
    args = parser.parse_args()

    if args.input_string is None:
        clipboard_content = get_clipboard_text()
        clean_content = clean_text(clipboard_content)
        output_string = to_lower_case(clean_content)
        set_clipboard_text(output_string)
    else:
        clean_input = clean_text(args.input_string)
        output_string = to_lower_case(clean_input)
        set_clipboard_text(output_string)

    print(output_string)

if __name__ == "__main__":
    main()