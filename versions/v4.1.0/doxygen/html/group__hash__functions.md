---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__hash__functions.html
original_path: doxygen/html/group__hash__functions.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hash Functions

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md)

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [sys\_hash\_func32\_t](#ga2566ca73d30b47ae66659e26fc985fad)) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | 32-bit Hash function interface |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32\_identity](#ga3bc327796b6836648e5dcf7c46cf38fa) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | The naive identity hash function. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32\_djb2](#gaaf45db9467193fe9e9d597537dd41c5e) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | Daniel J. Bernstein's hash function. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32\_murmur3](#gad35726d71600a63f4c3ac0382d0a3981) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | Murmur3 hash function. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32](#gadd3f6fd78ce2c0bf10e1c82a9c50f39d) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | System default 32-bit hash function. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga2566ca73d30b47ae66659e26fc985fad)sys\_hash\_func32\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* sys\_hash\_func32\_t) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| --- |

`#include <[hash_function.h](hash__function_8h.md)>`

32-bit Hash function interface

Hash functions are used to map data from an arbitrarily large space to a (typically smaller) fixed-size space. For a given input, a hash function will consistently generate the same, semi-unique numerical value. Even for marginally different data, a good hash function will distribute the entropy almost evenly over all bits in the hashed value when combined with modulo arithmetic over a finite-sized numeric field.

Parameters
:   | str | a string of input data |
    | --- | --- |
    | n | the number of bytes in `str` |

Returns
:   the numeric hash associated with `str`

## Function Documentation

## [◆ ](#gadd3f6fd78ce2c0bf10e1c82a9c50f39d)sys\_hash32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_hash32 | ( | const void \* | *str*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_function.h](hash__function_8h.md)>`

System default 32-bit hash function.

Parameters
:   | str | a string of input data |
    | --- | --- |
    | n | the number of bytes in `str` |

Returns
:   the numeric hash associated with `str`

## [◆ ](#gaaf45db9467193fe9e9d597537dd41c5e)sys\_hash32\_djb2()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_hash32\_djb2 | ( | const void \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) |

`#include <[hash_function.h](hash__function_8h.md)>`

Daniel J. Bernstein's hash function.

Some notes:

- normally, this hash function is used on NUL-terminated strings
- it has been modified to support arbitrary sequences of bytes
- it has been modified to use XOR rather than addition

Parameters
:   | str | a string of input data |
    | --- | --- |
    | n | the number of bytes in `str` |

Returns
:   the numeric hash associated with `str`

Note
:   enable with `CONFIG_SYS_HASH_FUNC32_DJB2`

See also
:   [https://theartincode.stanis.me/008-djb2/](https://theartincode.stanis.me/008-djb2/)

## [◆ ](#ga3bc327796b6836648e5dcf7c46cf38fa)sys\_hash32\_identity()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_hash32\_identity | ( | const void \* | *str*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_function.h](hash__function_8h.md)>`

The naive identity hash function.

This hash function requires that `n` is equal to the size of a primitive type, such as [u][int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6), [u][int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf), [u][int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2), [u][int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b), float, double, or void \*, and that the alignment of `str` agrees with that of the respective native type.

Note
:   The identity hash function is used for testing [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Parameters
:   | str | a string of input data |
    | --- | --- |
    | n | the number of bytes in `str` |

Returns
:   the numeric hash associated with `str`

## [◆ ](#gad35726d71600a63f4c3ac0382d0a3981)sys\_hash32\_murmur3()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_hash32\_murmur3 | ( | const void \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) |

`#include <[hash_function.h](hash__function_8h.md)>`

Murmur3 hash function.

Parameters
:   | str | a string of input data |
    | --- | --- |
    | n | the number of bytes in `str` |

Returns
:   the numeric hash associated with `str`

Note
:   enable with `CONFIG_SYS_HASH_FUNC32_MURMUR3`

See also
:   [https://en.wikipedia.org/wiki/MurmurHash](https://en.wikipedia.org/wiki/MurmurHash)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
