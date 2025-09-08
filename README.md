# Classic Ciphers in Python

This is a Python script I wrote to implement two classic ciphers: the Caesar cipher and the Vigenère cipher. The project started as a simple implementation and was refactored to incorporate a range of professional programming best practices. It can encrypt and decrypt text while preserving case and handling non-alphabetic characters.



## Features

- Encrypt and decrypt messages using either the Caesar or Vigenère cipher.
- Preserves the original letter casing of the text.
- Ignores non-alphabetic characters (spaces, punctuation, numbers), passing them through unchanged.
- Written with a focus on best practices: DRY principle, efficiency, and clear documentation.
- Includes full type hinting and input validation for robust, error-resistant operation.

## Requirements

This script uses only Python's standard library, so no external packages are needed. All you need is **Python 3.x** installed.

## Usage

To run the script with the built-in example, clone the repository and execute the file from your terminal:

```sh
python cipher.py
```

This will run the `main()` function and produce the following output, demonstrating both ciphers:

```
Offset: 3

Key: python

Original text: Hello, World! This is a test.

Caesar encrypted text: Khoor, Zruog! Wklv lv d whvw.

Caesar decrypted text: Hello, World! This is a test.

Vigenere encrypted text: Wiasl, Pldle! Kyic gc s hihx.

Vigenere decrypted text: Hello, World! This is a test.
```

## Code Overview

- **`_transform_character`**: The core helper function that handles the logic for shifting a single character while preserving its case.
- **`caesar` & `vigenere`**: The specific cipher implementations. They prepare the correct offset for each character and use the helper function to perform the transformation.
- **`encrypt` & `decrypt`**: These act as high-level dispatchers that validate inputs and call the correct cipher function based on the user's choice.
- **`main`**: Contains the example usage shown above.

## Technologies Used

- **Language:** Python 3
- **Modules:** `enum`, `string`, `typing` (all from the standard library)
