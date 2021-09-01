import random
import string

JOIN_SYMBOL = ','


def _create_encoding_data(s: str) -> dict:
    s += string.printable
    return dict(enumerate(s))


def _get_index_for_char(char: str, encoding_data: dict) -> int:
    possible_indexes = [index for index, base_char in encoding_data.items() if base_char == char]
    return random.choice(possible_indexes)


def encode(message: str, cipher: str) -> str:
    """Encode the message with the cipher."""
    encoding_data = _create_encoding_data(cipher)
    encoded_text = [str(_get_index_for_char(char, encoding_data)) for char in message]
    return JOIN_SYMBOL.join(encoded_text)


def decode(message: str, cipher: str) -> str:
    """Decode the message with the cipher."""
    encoding_data = _create_encoding_data(cipher)
    decoded_message = ''

    for index in message.split(JOIN_SYMBOL):
        decoded_message += encoding_data[int(index)]
    return decoded_message
