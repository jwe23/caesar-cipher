import nltk

# Ensure necessary NLTK resources are available.
nltk.download('words')

# Create a set containing all English words from the NLTK corpus.
english_words = set(nltk.corpus.words.words())

def decrypt_with_shift(ciphertext, shift, alphabet):
    """
    Decrypts a single Caesar cipher text using a specified shift value.

    Args:
      ciphertext (str): The encrypted text to decrypt.
      shift (int): The shift value to use for decryption.
      alphabet (str): The alphabet used for the decryption process.

    Returns:
      str: The decrypted text using the given shift.
    """
    decrypted_text = ""
    for char in ciphertext.lower():
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_index = (index - shift) % len(alphabet)
            decrypted_text += alphabet[decrypted_index]
        else:
            decrypted_text += char
    return decrypted_text

def caesar_brute_force(ciphertext):
    """
    Generates all possible plaintexts for a given Caesar cipher text by trying all possible shifts.

    Args:
      ciphertext (str): The text to decrypt.

    Returns:
      list: A list of all possible decrypted strings.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [decrypt_with_shift(ciphertext, shift, alphabet) for shift in range(len(alphabet))]

def caesar_brute_force_interactive(ciphertext):
    """
    Interactively attempts to decrypt a Caesar cipher text by showing all possible plaintexts to the user
    and asking for confirmation on the correct one.

    Args:
      ciphertext (str): The encrypted text to decrypt.

    Returns:
      str or None: The correctly decrypted text, or None if unable to validate decryption.
    """
    print("Attempting to decrypt. Please confirm if any of the decryptions is correct:\n")

    for decrypted_text in caesar_brute_force(ciphertext):
        if decrypted_text in english_words:
            user_input = input(f"Is '{decrypted_text}' correct? (y/n): ")
            if user_input.lower() == 'y':
                return decrypted_text

    return None

# User interaction to input the ciphertext and display the decryption.
ciphertext = input("Enter the encrypted word: ").strip()
decrypted_text = caesar_brute_force_interactive(ciphertext)

if decrypted_text:
    print(f"Decrypted word: {decrypted_text}")
else:
    print("No correct decryption found.")
