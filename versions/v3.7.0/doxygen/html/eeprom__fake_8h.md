---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/eeprom__fake_8h.html
original_path: doxygen/html/eeprom__fake_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eeprom\_fake.h File Reference

`#include <[zephyr/drivers/eeprom.h](eeprom_8h_source.md)>`  
`#include <[zephyr/fff.h](fff_8h_source.md)>`

[Go to the source code of this file.](eeprom__fake_8h_source.md)

| Functions | |
| --- | --- |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a1cb054262963a6627153371a2acfe402) (int, fake\_eeprom\_read, const struct [device](structdevice.md) \*, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f), void \*, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#aed5eb663ecbf3ca11fd70257c9e36613) (int, fake\_eeprom\_write, const struct [device](structdevice.md) \*, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f), const void \*, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ac45f5d2518a923c2c95f490f73b997cc) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9), fake\_eeprom\_size, const struct [device](structdevice.md) \*) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [fake\_eeprom\_size\_delegate](#a800769bebaa15f0430dd66078ea0c413) (const struct [device](structdevice.md) \*dev) |

## Function Documentation

## [◆ ](#a1cb054262963a6627153371a2acfe402)DECLARE\_FAKE\_VALUE\_FUNC() [1/3]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_eeprom\_read | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | , |
|  |  | void \* | , |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | ) |

## [◆ ](#aed5eb663ecbf3ca11fd70257c9e36613)DECLARE\_FAKE\_VALUE\_FUNC() [2/3]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_eeprom\_write | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | , |
|  |  | const void \* | , |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | ) |

## [◆ ](#ac45f5d2518a923c2c95f490f73b997cc)DECLARE\_FAKE\_VALUE\_FUNC() [3/3]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | , |
| --- | --- | --- | --- |
|  |  | fake\_eeprom\_size | , |
|  |  | const struct [device](structdevice.md) \* | ) |

## [◆ ](#a800769bebaa15f0430dd66078ea0c413)fake\_eeprom\_size\_delegate()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fake\_eeprom\_size\_delegate | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [eeprom](dir_af342b5e759e5b1b2dac755f05d42ced.md)
- [eeprom\_fake.h](eeprom__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
