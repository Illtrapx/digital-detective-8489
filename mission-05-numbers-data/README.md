# Mission 5 — Numbers and data

## 1. Task / objective

Work out conversions by hand, check them in Python, write a number converter and explain how text is encoded.

## 2. Work completed

Worked through all seven conversions and verified them in the Python interactive environment. Built [number_converter.py](number_converter.py) and checked three positive values, zero, a negative value and invalid text.

## 3. Commands / tools used

`python3 -q -i` opened the Python interactive environment for the checks below. `int(text, base)` reads digits in the supplied base. `bin()` and `hex()` return strings with the `0b` or `0x` prefix. `input()` reads a line from the terminal, `print()` displays each result and `ord()` returns a character's Unicode code point.

## 4. My understanding

### 5.1 Manual conversions

| Question | Working | Answer |
| --- | --- | --- |
| Decimal 13 to binary | 13 ÷ 2 = 6 r1, 6 ÷ 2 = 3 r0, 3 ÷ 2 = 1 r1, 1 ÷ 2 = 0 r1. Read the remainders from last to first. | `1101` |
| Decimal 25 to binary | 25 ÷ 2 = 12 r1, 12 ÷ 2 = 6 r0, 6 ÷ 2 = 3 r0, 3 ÷ 2 = 1 r1, 1 ÷ 2 = 0 r1. Read the remainders from last to first. | `11001` |
| Binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 8 + 2. | `10` |
| Binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 1. | `13` |
| Hexadecimal A to decimal | A represents ten in the ones place, so 10×1 = 10. | `10` |
| Hexadecimal 1F to decimal | F represents fifteen. 1×16 + 15×1 = 31. | `31` |
| Binary 1111 to hexadecimal | Four bits map to one hexadecimal digit. 8 + 4 + 2 + 1 = 15, and hexadecimal uses F for fifteen. | `F` |

In the division rows, `r` marks the remainder. Each binary place has twice the value of the place to its right. A group of eight bits is one byte.

### 5.2 Python verification

| Expression | REPL result | Matches manual working? |
| --- | --- | --- |
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `int("A", 16)` | `10` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(int("1111", 2))` | `'0xf'` | Yes |
| `hex(15)` | `'0xf'` | Yes |

Python writes hexadecimal letters in lowercase in `hex()`. The letter `f` represents the same digit as `F`.

### 5.3 Converter checks

From this directory, run `python3 number_converter.py` and enter a whole decimal number. The program parses the input once, then passes that integer to `bin()` and `hex()`.

| Decimal input | Binary output | Hexadecimal output |
| --- | --- | --- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |
| 0 | `0b0` | `0x0` |
| -15 | `-0b1111` | `-0xf` |

Entering `hello` printed `Please enter a whole number in base 10.` and exited.

### 5.4 Text encoding

`ord("A")` gave 65, and `ord("a")` gave 97. These values are the ASCII codes for those letters. A shared encoding lets a program turn text into bytes and lets another program recover the same text from those bytes. The character `é` is outside basic ASCII and uses two bytes in UTF-8.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[number_converter.py](number_converter.py), the manual working, the verified REPL results and the converter test table above.

## 8. Commit details

`Build number converter and practise data representation`. [GitHub commit history](https://github.com/Illtrapx/digital-detective-8489/commits/main/).
