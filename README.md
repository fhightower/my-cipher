# My Cipher

A simple, effective cipher I created for fun.

## Usage

### Encode

To encode a message using this cipher, you'll need two strings:

1. A message
2. A cipher text used to encode the message

You encode like:

```python
import cipher

message = 'What hath God wrought?'
cipher_text = 'the quick brown fox jumps over the lazy dog'

cipher.encode(message, cipher_text)
```

### Decode

To decode, you'll need:

1. An encoded message
2. A cipher text (the same one used to encode it)

You can decode something like:

```python
import cipher

encoded_message = '101,32,36,72,30,60,53,72,32,39,85,12,56,3,13,11,41,21,42,60,72,125'
cipher_text = 'the quick brown fox jumps over the lazy dog'

cipher.decode(encoded_message, cipher_text)
```
