---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__eeprom__interface.html
original_path: doxygen/html/group__eeprom__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

EEPROM Interface

[Device Driver APIs](group__io__interfaces.md)

EEPROM Interface.
[More...](#details)

| Functions | |
| --- | --- |
| int | [eeprom\_read](#ga92b92c8fb721f1b94038a20443d46e52) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read data from EEPROM. |
| int | [eeprom\_write](#ga1973e8982de88f53e49154dc73461e56) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write data to EEPROM. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [eeprom\_get\_size](#ga27a1f50af8916f9291dad4a63796a707) (const struct [device](structdevice.md) \*dev) |
|  | Get the size of the EEPROM in bytes. |

## Detailed Description

EEPROM Interface.

## Function Documentation

## [◆ ](#ga27a1f50af8916f9291dad4a63796a707)eeprom\_get\_size()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) eeprom\_get\_size | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[eeprom.h](eeprom_8h.md)>`

Get the size of the EEPROM in bytes.

Parameters
:   | dev | EEPROM device. |
    | --- | --- |

Returns
:   EEPROM size in bytes.

## [◆ ](#ga92b92c8fb721f1b94038a20443d46e52)eeprom\_read()

| int eeprom\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[eeprom.h](eeprom_8h.md)>`

Read data from EEPROM.

Parameters
:   | dev | EEPROM device |
    | --- | --- |
    | offset | Address offset to read from. |
    | data | Buffer to store read data. |
    | len | Number of bytes to read. |

Returns
:   0 on success, negative errno code on failure.

## [◆ ](#ga1973e8982de88f53e49154dc73461e56)eeprom\_write()

| int eeprom\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[eeprom.h](eeprom_8h.md)>`

Write data to EEPROM.

Parameters
:   | dev | EEPROM device |
    | --- | --- |
    | offset | Address offset to write data to. |
    | data | Buffer with data to write. |
    | len | Number of bytes to write. |

Returns
:   0 on success, negative errno code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
