# Caesar Cipher Decryption Tool

This tool provides an implementation of the Caesar cipher decryption process. It includes a brute force decryption function that tries all possible shift values to find valid English words and an interactive component that allows users to confirm the correct decryption.

## Features

- Brute force decryption of Caesar cipher without the need for the shift value.
- Interactive validation of possible decrypted outputs.
- Utilizes the NLTK words corpus to verify English words.

## Requirements

- Python 3.x
- NLTK library

## Installation

Before you can use the Caesar cipher decryption tool, you need to set up your environment:

```bash
# Clone this repository
git clone https://github.com/jwe23/caesar-cipher.git
cd your_repository_folder

# Install NLTK
pip install nltk
```
## Usage
To use the decryption tool, run the script from your command line:

```bash
cd ~/caesar-cipher/
python encryption.py
```
Follow the interactive prompts to input the encrypted text and validate the potential decrypted outputs.

## Example
```bash
Enter the encrypted word: xyz
Attempting to decrypt. Please confirm if any of the decryptions is correct:

Is 'bcd' correct? (y/n): n
Is 'xyz' correct? (y/n): y
```
The program uses NLP to determine if the input is a word but in smaller words there might be duplicates so the program verifies with the user. 
