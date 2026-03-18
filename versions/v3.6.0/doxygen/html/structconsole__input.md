---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structconsole__input.html
original_path: doxygen/html/structconsole__input.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console\_input Struct Reference

Console input representation.
[More...](#details)

`#include <[console.h](drivers_2console_2console_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_mcumgr](#a2c13a1e2a4895cf1d51c8ce7879af927): 1 |
|  | Whether this is an mcumgr command. |
| char | [line](#a33bf8ba6d114ec99219c134c0f6c3474) [CONFIG\_CONSOLE\_INPUT\_MAX\_LINE\_LEN] |
|  | Buffer where the input line is recorded. |

## Detailed Description

Console input representation.

This struct is used to represent an input line from a console. Recorded line must be NULL terminated.

## Field Documentation

## [◆ ](#a2c13a1e2a4895cf1d51c8ce7879af927)is\_mcumgr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) console\_input::is\_mcumgr |
| --- |

Whether this is an mcumgr command.

## [◆ ](#a33bf8ba6d114ec99219c134c0f6c3474)line

| char console\_input::line[CONFIG\_CONSOLE\_INPUT\_MAX\_LINE\_LEN] |
| --- |

Buffer where the input line is recorded.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/console/[console.h](drivers_2console_2console_8h_source.md)

- [console\_input](structconsole__input.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
