def caesar_cipher(text, shift, alphabet):
    """
    Encrypts or decrypts a given text using the Caesar cipher with a specified shift on a given alphabet.

    Args:
      text (str): The string to encrypt or decrypt.
      shift (int): The number of positions to shift each character (positive for encryption, negative for decryption).
      alphabet (str): The alphabet to use for the shift.

    Returns:
      str: The resulting encrypted or decrypted string.
    """

    # Initialize the result variable to store the processed text
    result_text = ""

    # Iterate over each character in the input text
    for char in text:
        if char in alphabet:
            # Find the character's position in the alphabet and apply the shift
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % len(alphabet)
            result_text += alphabet[new_index]
        else:
            # If the character is not in the alphabet, leave it unchanged
            result_text += char

    return result_text

# Define the English alphabet
english_alphabet = "abcdefghijklmnopqrstuvwxyz"

# Prompt the user for text and shift value
input_text = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value: "))

# Encrypt the text
encrypted_text = caesar_cipher(input_text, shift_value, english_alphabet)
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = caesar_cipher(encrypted_text, -shift_value, english_alphabet)
print("Decrypted text:", decrypted_text)
