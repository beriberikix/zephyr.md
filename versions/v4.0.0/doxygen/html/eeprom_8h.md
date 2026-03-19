---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/eeprom_8h.html
original_path: doxygen/html/eeprom_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eeprom.h File Reference

Public API for EEPROM drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/eeprom.h>`

[Go to the source code of this file.](eeprom_8h_source.md)

| Functions | |
| --- | --- |
| int | [eeprom\_read](group__eeprom__interface.md#ga92b92c8fb721f1b94038a20443d46e52) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read data from EEPROM. |
| int | [eeprom\_write](group__eeprom__interface.md#ga1973e8982de88f53e49154dc73461e56) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write data to EEPROM. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [eeprom\_get\_size](group__eeprom__interface.md#ga27a1f50af8916f9291dad4a63796a707) (const struct [device](structdevice.md) \*dev) |
|  | Get the size of the EEPROM in bytes. |

## Detailed Description

Public API for EEPROM drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [eeprom.h](eeprom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
