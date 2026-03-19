---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unionemul_1_1bus.html
original_path: doxygen/html/unionemul_1_1bus.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul::bus Union Reference

Pointer to the emulated bus node.
[More...](#details)

`#include <[emul.h](drivers_2emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [i2c\_emul](structi2c__emul.md) \* | [i2c](#a1f2079251cce4ffa92d3f1a4315b7b42) |
| struct [espi\_emul](structespi__emul.md) \* | [espi](#adbf407e15fbfe3da70b0c458e8edcf8d) |
| struct [spi\_emul](structspi__emul.md) \* | [spi](#aa9e71864d3e4a0df64ed785522f29139) |
| struct [mspi\_emul](structmspi__emul.md) \* | [mspi](#ab88888ce5358ad5fa016cc5fe01ed98c) |
| struct [uart\_emul](structuart__emul.md) \* | [uart](#a4201a6d0980f539343936df40a5f7ca9) |
| struct [no\_bus\_emul](structno__bus__emul.md) \* | [none](#a6a8ad4e1e183a81c05b64b5c87cfa25a) |

## Detailed Description

Pointer to the emulated bus node.

## Field Documentation

## [◆ ](#adbf407e15fbfe3da70b0c458e8edcf8d)espi

| struct [espi\_emul](structespi__emul.md)\* emul::bus::espi |
| --- |

## [◆ ](#a1f2079251cce4ffa92d3f1a4315b7b42)i2c

| struct [i2c\_emul](structi2c__emul.md)\* emul::bus::i2c |
| --- |

## [◆ ](#ab88888ce5358ad5fa016cc5fe01ed98c)mspi

| struct [mspi\_emul](structmspi__emul.md)\* emul::bus::mspi |
| --- |

## [◆ ](#a6a8ad4e1e183a81c05b64b5c87cfa25a)none

| struct [no\_bus\_emul](structno__bus__emul.md)\* emul::bus::none |
| --- |

## [◆ ](#aa9e71864d3e4a0df64ed785522f29139)spi

| struct [spi\_emul](structspi__emul.md)\* emul::bus::spi |
| --- |

## [◆ ](#a4201a6d0980f539343936df40a5f7ca9)uart

| struct [uart\_emul](structuart__emul.md)\* emul::bus::uart |
| --- |

---

The documentation for this union was generated from the following file:

- zephyr/drivers/[emul.h](drivers_2emul_8h_source.md)

- [emul](structemul.md)
- [bus](unionemul_1_1bus.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
