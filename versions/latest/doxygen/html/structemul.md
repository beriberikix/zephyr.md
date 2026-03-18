---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structemul.html
original_path: doxygen/html/structemul.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

An emulator instance - represents the *target* emulated device/peripheral that is interacted with through an emulated bus.
[More...](#details)

`#include <[emul.h](emul_8h_source.md)>`

| Data Structures | |
| --- | --- |
| union | [bus](unionemul_1_1bus.md) |
|  | Pointer to the emulated bus node. [More...](unionemul_1_1bus.md#details) |

| Data Fields | |
| --- | --- |
| [emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50) | [init](#a5ec4e292613d2d79d6bd57fe6cd5b41b) |
|  | function used to initialise the emulator state |
| const struct [device](structdevice.md) \* | [dev](#a4159ce815a6b4022bf35cbd0d0102bba) |
|  | handle to the device for which this provides low-level emulation |
| const void \* | [cfg](#ae6f86e44a6b28296528d607124f4b812) |
|  | Emulator-specific configuration data. |
| void \* | [data](#a82f3fcaf221cd329ef1b6cb93cc7c8e6) |
|  | Emulator-specific data. |
| enum [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) | [bus\_type](#a92a4811a8656b8f0c3f3c7873918da3c) |
|  | The bus type that the emulator is attached to. |
| union emul::bus | [bus](#a9f3ec93d05fdf287069dbb0aa48cc8ac) |
| const void \* | [backend\_api](#ac7e90a7ff00a0c08836821c7d49b7dea) |
|  | Address of the API structure exposed by the emulator instance. |

## Detailed Description

An emulator instance - represents the *target* emulated device/peripheral that is interacted with through an emulated bus.

Instances of emulated bus nodes (e.g. [i2c\_emul](structi2c__emul.md "Node in a linked list of emulators for I2C devices.")) and emulators (i.e. struct emul) are exactly 1..1

## Field Documentation

## [◆ ](#ac7e90a7ff00a0c08836821c7d49b7dea)backend\_api

| const void\* emul::backend\_api |
| --- |

Address of the API structure exposed by the emulator instance.

## [◆ ](#a9f3ec93d05fdf287069dbb0aa48cc8ac)bus

| union emul::bus emul::bus |
| --- |

## [◆ ](#a92a4811a8656b8f0c3f3c7873918da3c)bus\_type

| enum [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) emul::bus\_type |
| --- |

The bus type that the emulator is attached to.

## [◆ ](#ae6f86e44a6b28296528d607124f4b812)cfg

| const void\* emul::cfg |
| --- |

Emulator-specific configuration data.

## [◆ ](#a82f3fcaf221cd329ef1b6cb93cc7c8e6)data

| void\* emul::data |
| --- |

Emulator-specific data.

## [◆ ](#a4159ce815a6b4022bf35cbd0d0102bba)dev

| const struct [device](structdevice.md)\* emul::dev |
| --- |

handle to the device for which this provides low-level emulation

## [◆ ](#a5ec4e292613d2d79d6bd57fe6cd5b41b)init

| [emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50) emul::init |
| --- |

function used to initialise the emulator state

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[emul.h](emul_8h_source.md)

- [emul](structemul.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
