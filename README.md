# Lowercase Utility

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](https://github.com/voothi/20240327132411-lowercase-util)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight utility for converting text to lowercase, cleaning up HTML tags, and normalizing spacing from the clipboard or terminal.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Building from Source](#building-from-source)
- [AutoHotkey Integration](#autohotkey-integration)
- [Kardenwort Ecosystem](#kardenwort-ecosystem)
- [License](#license)

---

## Description
`lowercase-util` is a focused tool that processes text to ensure it is in lowercase and free from unwanted formatting characters. It is particularly useful when preparing text for search engines, databases, or documents that require a consistent lowercase format.

[Return to Top](#lowercase-utility)

## Features
- **Lowercase Conversion**: Automatically converts all input text to lowercase.
- **HTML Cleanup**: Removes HTML tags and special entities often found in clipboard content from web sources.
- **Control Character Removal**: Strips non-printable and control characters.
- **Newline Normalization**: Joins single lines while preserving paragraph breaks (newlines followed by whitespace).
- **Clipboard Integration**: Seamlessly reads from and writes back to the system clipboard.

[Return to Top](#lowercase-utility)

## Installation

### Using Python (Primary Method)
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pyperclip
   ```
3. Run the script:
   ```bash
   python lowercase_util.py
   ```

[Return to Top](#lowercase-utility)

## Usage

1. **Option A (Clipboard)**: Copy text to your clipboard and run the script without arguments:
   ```powershell
   python u:\voothi\20240327132411-lowercase-util\lowercase_util.py
   ```
   The cleaned text will be written back to your clipboard.

2. **Option B (Command Line)**: Pass the text as a command line argument:
   ```powershell
   python u:\voothi\20240327132411-lowercase-util\lowercase_util.py "TEXT TO CONVERT"
   ```

[Return to Top](#lowercase-utility)

## Building from Source

For a standalone executable, you can use PyInstaller:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller==5.13.2
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole lowercase_util.py
   ```
The executable will be located in the `dist/` directory.

[Return to Top](#lowercase-utility)

## AutoHotkey Integration

For a more seamless workflow, you can use the **[lowercase.ahk](https://github.com/voothi/20240411110510-autohotkey/blob/main/lowercase.ahk)** script. 

This script maps the process to `Ctrl + Alt + I` (^!I), performing the following steps automatically:
1. **Copies** the currently selected text.
2. **Processes** it through the Python script.
3. **Pastes** the converted lowercase text back into your active window.

> [!IMPORTANT]
> You must update the paths in the `RunWait` command within the `.ahk` script to match your local installation of Python and the location of `lowercase_util.py`.

[Return to Top](#lowercase-utility)

## Kardenwort Ecosystem

This project is part of the **[Kardenwort](https://github.com/kardenwort)** environment, designed to create a focused and efficient learning ecosystem.

[Return to Top](#table-of-contents)

## License
MIT License. See LICENSE file for details.

[Return to Top](#lowercase-utility)
