# Classical Ciphers

Python implementations of four classical encryption techniques, written while studying cryptography. Each program takes input from the keyboard, encrypts it, then decrypts it again to show the original text.

## Programs

| File | What it does |
|---|---|
| `caesar_cipher.py` | Caesar shift of 1 on a single letter, then shifts it back |
| `vigenere_cipher.py` | Vigenere cipher with a repeating keyword; spaces are removed before encrypting and restored after decrypting |
| `playfair.py` | Playfair cipher: builds a 5x5 key square, encrypts letter pairs, then decrypts |
| `onetimepad.py` | One-time pad style cipher using a random key as long as the message |

## Requirements

Python 3. No extra libraries.

## Run

```
python caesar_cipher.py
python vigenere_cipher.py
python playfair.py
python onetimepad.py
```

## Example runs

**Vigenere** (plain text `attack at dawn`, key `lemon`)
```
Cipher text is:  LXFOPVEFRNHR
Plain text is:  attack at dawn
```

**Playfair** (key `monarchy`, word `instruments`)
```
the cipher text is: GATLMZCLRQXA
```

**One-time pad** (the key is random, so it changes on every run)
```
the key is:  ISSTE
the ciphertext is:  PWDES
the plaintext was:  hello
```

## How each one works

- **Caesar:** each letter moves a fixed number of places in the alphabet. This program uses a shift of 1 and wraps around with `% 26`.
- **Vigenere:** like Caesar, but the shift changes for each letter based on the repeating keyword (`a = 0`, `b = 1`, and so on).
- **Playfair:** the key square is built from the keyword followed by the remaining letters, with I and J sharing one cell (enter I in place of J). Text is split into pairs, and a filler letter (X) separates repeated letters or pads an odd ending. Each pair is encrypted by the row, column, or rectangle rule.
- **One-time pad:** a random key the same length as the message is added to the message letters modulo 26.

## Limitations

- Letters only: numbers and punctuation are not handled.
- Playfair leaves the filler letter in the decrypted text, so `instruments` comes back as `INSTRUMENTSX`.
- The one-time pad uses Python's `random` module, which is **not cryptographically secure**. A real one-time pad needs a truly random key that is never reused. For anything real, the `secrets` module is the right tool.
- All of these ciphers are historical and easy to break today. This repo is for learning, not for protecting data.

## Author

Tanishq Gyaneshwar Dhoke ([@Tainydaug](https://github.com/Tainydaug))
