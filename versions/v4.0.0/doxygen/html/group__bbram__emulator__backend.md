---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bbram__emulator__backend.html
original_path: doxygen/html/group__bbram__emulator__backend.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BBRAM emulator backend API

[Device Driver APIs](group__io__interfaces.md)

BBRAM emulator backend API.
[More...](#details)

| Functions | |
| --- | --- |
| static int | [emul\_bbram\_backend\_set\_data](#gaeff1fa9acd765323778c42a4c3424c0b) (const struct [emul](structemul.md) \*target, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Set the expected data in the bbram region. |
| static int | [emul\_bbram\_backend\_get\_data](#ga92942f1ebe6905ad3cfe389824af5914) (const struct [emul](structemul.md) \*target, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Get the expected data in the bbram region. |

## Detailed Description

BBRAM emulator backend API.

## Function Documentation

## [◆ ](#ga92942f1ebe6905ad3cfe389824af5914)emul\_bbram\_backend\_get\_data()

| | int emul\_bbram\_backend\_get\_data | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_bbram.h](emul__bbram_8h.md)>`

Get the expected data in the bbram region.

Parameters
:   | target | Pointer to the emulator instance to operate on |
    | --- | --- |
    | offset | Offset within the memory to get |
    | count | Number of bytes to read |
    | data | The data buffer to hold the result |

Returns
:   0 if successful
:   -ENOTSUP if no backend API or if the get\_data function isn't implemented
:   -ERANGE if the address is out of range.

## [◆ ](#gaeff1fa9acd765323778c42a4c3424c0b)emul\_bbram\_backend\_set\_data()

| | int emul\_bbram\_backend\_set\_data | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_bbram.h](emul__bbram_8h.md)>`

Set the expected data in the bbram region.

Parameters
:   | target | Pointer to the emulator instance to operate on |
    | --- | --- |
    | offset | Offset within the memory to set |
    | count | Number of bytes to write |
    | data | The data to write |

Returns
:   0 if successful
:   -ENOTSUP if no backend API or if the set\_data function isn't implemented
:   -ERANGE if the destination address is out of range.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
