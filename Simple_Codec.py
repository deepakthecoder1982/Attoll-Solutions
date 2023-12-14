def encode(word):
    encoded = ""
    for i, letter in enumerate(word):
        if i % 2 == 0:  # Even numbered letters
            encoded += letter + chr(155 - ord(letter))  # Appending the letter and its opposite
        else:  # Odd numbered letters
            encoded += chr(155 - ord(letter))  # Appending the alphabetic opposite
    return encoded

def decode(encoded_word):
    decoded = ""
    for i in range(0, len(encoded_word), 2):
        letter = encoded_word[i]
        if i + 1 < len(encoded_word):  # Check if there's a pair of characters
            opposite = encoded_word[i + 1]
            decoded += opposite if ord(opposite) + ord(letter) == 155 else letter
        else:
            decoded += letter
    return decoded

# Test cases
test_cases = [
    ("ABC", "ZBYX"),
    ("XYZ", "XCBZA"),
    ("GHI", "THSR"),
    ("NOP", "NMLPK"),
    ("JKL", "JQPLO"),
    ("UTS", "FTGH")
]

for word, expected_encoded in test_cases:
    encoded_result = encode(word)
    decoded_result = decode(encoded_result)
    print(f"Input data: {word}, Encoded: {encoded_result}, Decoded: {decoded_result}")
