---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__base64.html
original_path: doxygen/html/group__base64.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Base64

[Utilities](group__utilities.md)

Base64 encoding/decoding functions.
[More...](#details)

| Functions | |
| --- | --- |
| int | [base64\_encode](#gaaff09edf41470c26d5a54d18c4f91ba0) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*olen, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) slen) |
|  | Encode a buffer into base64 format. |
| int | [base64\_decode](#ga9e84f3adc54120fb1f1ccffb1bac8c5c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*olen, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) slen) |
|  | Decode a base64-formatted buffer. |

## Detailed Description

Base64 encoding/decoding functions.

## Function Documentation

## [◆ ](#ga9e84f3adc54120fb1f1ccffb1bac8c5c)base64\_decode()

| int base64\_decode | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dst*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *dlen*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *olen*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *slen* ) |

`#include <[base64.h](base64_8h.md)>`

Decode a base64-formatted buffer.

Parameters
:   | dst | destination buffer (can be NULL for checking size) |
    | --- | --- |
    | dlen | size of the destination buffer |
    | olen | number of bytes written |
    | src | source buffer |
    | slen | amount of data to be decoded |

Returns
:   0 if successful, -ENOMEM, or -EINVAL if the input data is not correct. \*olen is always updated to reflect the amount of data that has (or would have) been written.

Note
:   Call this function with \*dst = NULL or dlen = 0 to obtain the required buffer size in \*olen

## [◆ ](#gaaff09edf41470c26d5a54d18c4f91ba0)base64\_encode()

| int base64\_encode | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dst*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *dlen*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *olen*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *slen* ) |

`#include <[base64.h](base64_8h.md)>`

Encode a buffer into base64 format.

Parameters
:   | dst | destination buffer |
    | --- | --- |
    | dlen | size of the destination buffer |
    | olen | number of bytes written |
    | src | source buffer |
    | slen | amount of data to be encoded |

Returns
:   0 if successful, or -ENOMEM if the buffer is too small. \*olen is always updated to reflect the amount of data that has (or would have) been written. If that length cannot be represented, then no data is written to the buffer and \*olen is set to the maximum length representable as a size\_t.

Note
:   Call this function with dlen = 0 to obtain the required buffer size in \*olen

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
