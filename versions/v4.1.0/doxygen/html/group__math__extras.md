---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__math__extras.html
original_path: doxygen/html/group__math__extras.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Math extras

[Utilities](group__utilities.md)

Extra arithmetic and bit manipulation functions.
[More...](#details)

| Unsigned integer addition with overflow detection. | |
| --- | --- |
| These functions compute a + b and store the result in \*result, returning true if the operation overflowed. | |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u16\_add\_overflow](#ga62d018abdf97551665cab7486b5a519a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
|  | Add two unsigned 16-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u32\_add\_overflow](#ga3f36aa272f5595d78c6e8219b2c4dbfb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Add two unsigned 32-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u64\_add\_overflow](#gaf98ec1d8b1c00e30382eed01853e3307) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result) |
|  | Add two unsigned 64-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [size\_add\_overflow](#ga7aaec179564038b540aaf4ab3c9a666d) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) a, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
|  | Add two size\_t integers. |

| Unsigned integer multiplication with overflow detection. | |
| --- | --- |
| These functions compute a \* b and store the result in \*result, returning true if the operation overflowed. | |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u16\_mul\_overflow](#ga292df7083a9da5525cda13e2546e81ba) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
|  | Multiply two unsigned 16-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u32\_mul\_overflow](#ga427e8cd4fcafab244576994acc9b960f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Multiply two unsigned 32-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u64\_mul\_overflow](#ga366f6606874071677bf9079647d9abce) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result) |
|  | Multiply two unsigned 64-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [size\_mul\_overflow](#ga790b24a5d239afcc08d9e4f66c25ea56) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) a, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
|  | Multiply two size\_t integers. |

| Count leading zeros. | |
| --- | --- |
| Count the number of leading zero bits in the bitwise representation of x.  When x = 0, this is the size of x in bits. | |
| static int | [u32\_count\_leading\_zeros](#ga97e8d8a40a45899ab7e5ce718342536b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
|  | Count the number of leading zero bits in a 32-bit integer. |
| static int | [u64\_count\_leading\_zeros](#gaf5f31e98f2f675a0b4cc54b7fba6f56c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x) |
|  | Count the number of leading zero bits in a 64-bit integer. |

| Count trailing zeros. | |
| --- | --- |
| Count the number of trailing zero bits in the bitwise representation of x.  When x = 0, this is the size of x in bits. | |
| static int | [u32\_count\_trailing\_zeros](#ga4cb313f98c3fd3b00d6f4db74a9a0076) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
|  | Count the number of trailing zero bits in a 32-bit integer. |
| static int | [u64\_count\_trailing\_zeros](#ga300356629c0388d37958ef026180ea4d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x) |
|  | Count the number of trailing zero bits in a 64-bit integer. |

## Detailed Description

Extra arithmetic and bit manipulation functions.

Portable wrapper functions for a number of arithmetic and bit-counting functions that are often provided by compiler builtins. If the compiler does not have an appropriate builtin, a portable C implementation is used instead.

## Function Documentation

## [◆ ](#ga7aaec179564038b540aaf4ab3c9a666d)size\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) size\_add\_overflow | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *a*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *b*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Add two size\_t integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#ga790b24a5d239afcc08d9e4f66c25ea56)size\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) size\_mul\_overflow | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *a*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *b*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Multiply two size\_t integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#ga62d018abdf97551665cab7486b5a519a)u16\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u16\_add\_overflow | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *a*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *b*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Add two unsigned 16-bit integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#ga292df7083a9da5525cda13e2546e81ba)u16\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u16\_mul\_overflow | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *a*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *b*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Multiply two unsigned 16-bit integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#ga3f36aa272f5595d78c6e8219b2c4dbfb)u32\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u32\_add\_overflow | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *a*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *b*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Add two unsigned 32-bit integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#ga97e8d8a40a45899ab7e5ce718342536b)u32\_count\_leading\_zeros()

| | int u32\_count\_leading\_zeros | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Count the number of leading zero bits in a 32-bit integer.

Parameters
:   | x | Integer to count leading zeros in. |
    | --- | --- |

Returns
:   Number of leading zero bits in x.

## [◆ ](#ga4cb313f98c3fd3b00d6f4db74a9a0076)u32\_count\_trailing\_zeros()

| | int u32\_count\_trailing\_zeros | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Count the number of trailing zero bits in a 32-bit integer.

Parameters
:   | x | Integer to count trailing zeros in. |
    | --- | --- |

Returns
:   Number of trailing zero bits in x.

## [◆ ](#ga427e8cd4fcafab244576994acc9b960f)u32\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u32\_mul\_overflow | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *a*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *b*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Multiply two unsigned 32-bit integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#gaf98ec1d8b1c00e30382eed01853e3307)u64\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u64\_add\_overflow | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *a*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *b*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Add two unsigned 64-bit integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

## [◆ ](#gaf5f31e98f2f675a0b4cc54b7fba6f56c)u64\_count\_leading\_zeros()

| | int u64\_count\_leading\_zeros | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Count the number of leading zero bits in a 64-bit integer.

Parameters
:   | x | Integer to count leading zeros in. |
    | --- | --- |

Returns
:   Number of leading zero bits in x.

## [◆ ](#ga300356629c0388d37958ef026180ea4d)u64\_count\_trailing\_zeros()

| | int u64\_count\_trailing\_zeros | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Count the number of trailing zero bits in a 64-bit integer.

Parameters
:   | x | Integer to count trailing zeros in. |
    | --- | --- |

Returns
:   Number of trailing zero bits in x.

## [◆ ](#ga366f6606874071677bf9079647d9abce)u64\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u64\_mul\_overflow | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *a*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *b*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *result* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[math_extras.h](math__extras_8h.md)>`

Multiply two unsigned 64-bit integers.

Parameters
:   | a | First operand. |
    | --- | --- |
    | b | Second operand. |
    | result | Pointer to the result. |

Returns
:   true if the operation overflowed.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
