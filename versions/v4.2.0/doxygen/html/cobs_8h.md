---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cobs_8h.html
original_path: doxygen/html/cobs_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cobs.h File Reference

`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`

[Go to the source code of this file.](cobs_8h_source.md)

| Macros | |
| --- | --- |
| #define | [COBS\_DEFAULT\_DELIMITER](#a67d201df9cea6c681ed537516dd1d35e)   0x00 |
| #define | [COBS\_FLAG\_TRAILING\_DELIMITER](#a016e001ca84dae52391b5bc22b5c92ad)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Flag indicating that encode and decode should include an implicit end delimiter. |
| #define | [COBS\_FLAG\_CUSTOM\_DELIMITER](#a5e05dfb0ac63e51372805f2241c90491)(x) |
|  | Macro for extracting delimiter from flags. |

| Functions | |
| --- | --- |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [cobs\_max\_encoded\_len](group__cobs.md#ga71047f135e408e95d83828e898e823b0) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) decoded\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Calculate maximum encoded buffer size. |
| int | [cobs\_encode](group__cobs.md#gadf39d47a13fe1e3b10bcc9208f5b4786) (struct [net\_buf](structnet__buf.md) \*src, struct [net\_buf](structnet__buf.md) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Standard COBS encoding. |
| int | [cobs\_decode](group__cobs.md#gabb6193b8d15b33e5c739c9609376950f) (struct [net\_buf](structnet__buf.md) \*src, struct [net\_buf](structnet__buf.md) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Standard COBS decoding. |

## Macro Definition Documentation

## [◆ ](#a67d201df9cea6c681ed537516dd1d35e)COBS\_DEFAULT\_DELIMITER

| #define COBS\_DEFAULT\_DELIMITER   0x00 |
| --- |

## [◆ ](#a5e05dfb0ac63e51372805f2241c90491)COBS\_FLAG\_CUSTOM\_DELIMITER

| #define COBS\_FLAG\_CUSTOM\_DELIMITER | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & 0xff)

Macro for extracting delimiter from flags.

8 LSB of "flags" is used for the delimiter Example usage: cobs\_encode(src\_buf, dst\_buf, COBS\_FLAG\_TRAILING\_DELIMITER | [COBS\_FLAG\_CUSTOM\_DELIMITER(0x7F)](#a5e05dfb0ac63e51372805f2241c90491));

## [◆ ](#a016e001ca84dae52391b5bc22b5c92ad)COBS\_FLAG\_TRAILING\_DELIMITER

| #define COBS\_FLAG\_TRAILING\_DELIMITER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

Flag indicating that encode and decode should include an implicit end delimiter.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [cobs.h](cobs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
