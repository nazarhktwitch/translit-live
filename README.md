# Transliteration and Keyboard Input Interception

## Overview
This Python program transliterates text from Cyrillic to Latin in real time while intercepting keyboard input. It allows users to type in any application (e.g., Telegram, Minecraft), transliterate the text, and copy the result to the clipboard upon pressing Enter.

## Features
- **Real-time keyboard input interception**: Captures keystrokes and stores them in a buffer.
- 
- **Cyrillic to Latin transliteration**: Converts text based on a predefined transliteration table.
- 
- **Clipboard integration**: Automatically copies transliterated text to the clipboard.
- 
- **Hotkeys**:
- 
  - `Enter`: Executes transliteration and clears the buffer.
  - 
  - `Backspace`: Removes the last character from the buffer.
  - 
  - `Esc`: Exits the program.

## Requirements
- Python 3.6+
- Required libraries:
  - `pynput`
  - `pyperclip`

Install dependencies with:
```bash
pip install pynput pyperclip
```

## Usage
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/translit-interceptor.git
   cd translit-interceptor
   ```

2. Run the script:
   ```bash
   python translit_interceptor.py
   ```

3. Start typing in any application. When you press `Enter`, the transliterated text will be displayed in the console and copied to the clipboard.

## Transliteration Table
The program uses the following mapping for transliteration:

| Cyrillic | Latin | Cyrillic | Latin |
|----------|-------|----------|-------|
| а        | a     | А        | A     |
| б        | b     | Б        | B     |
| в        | v     | В        | V     |
| г        | g     | Г        | G     |
| д        | d     | Д        | D     |
| е        | e     | Е        | E     |
| ё        | yo    | Ё        | Yo    |
| ж        | zh    | Ж        | Zh    |
| з        | z     | З        | Z     |
| и        | i     | И        | I     |
| й        | y     | Й        | Y     |
| ...      | ...   | ...      | ...   |

For the full table, see the source code.

## Example
### Input
```
Привет, как дела?
```

### Output
```
Privet, kak dela?
```

The transliterated text will also be available in your clipboard.

## Limitations
- The program does not support real-time text replacement in other applications.
  
- Special characters and unsupported symbols are left unchanged.

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue for feature requests and bug reports.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The [pynput](https://pypi.org/project/pynput/) library for keyboard interception.
  
- The [pyperclip](https://pypi.org/project/pyperclip/) library for clipboard management.
