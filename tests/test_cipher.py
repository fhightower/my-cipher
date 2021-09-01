import cipher

TEST_MESSAGE = 'What hath God wrought?'
TEST_CIPHER_TEXT = 'the quick brown fox jumps over the lazy dog'


def test_encode_and_decode():
    assert cipher.decode(cipher.encode(TEST_MESSAGE, TEST_CIPHER_TEXT), TEST_CIPHER_TEXT) == TEST_MESSAGE
