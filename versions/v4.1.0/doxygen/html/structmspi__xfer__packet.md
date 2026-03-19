---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__xfer__packet.html
original_path: doxygen/html/structmspi__xfer__packet.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_xfer\_packet Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Transfer API](group__mspi__transfer__api.md)

MSPI peripheral xfer packet format.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mspi\_xfer\_direction](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6) | [dir](#afb408ea48ff8863c9714d39c4f7c8a2c) |
|  | Direction (Transmit/Receive). |
| enum [mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) | [cb\_mask](#aedc8eadfb3a0737c3984b130ec21d96c) |
|  | Bus event callback masks. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cmd](#a2717e86b7fbb01be65a4955a8e26ebc0) |
|  | Transfer command. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [address](#a08dae9b6fbda60f06430cb2b842280b9) |
|  | Transfer Address. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_bytes](#a050a827d0ee0349cd7a006de20b1db0c) |
|  | Number of bytes to transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data\_buf](#a0b7b3d68ff46173378e4076b439e35ac) |
|  | Data Buffer. |

## Detailed Description

MSPI peripheral xfer packet format.

## Field Documentation

## [◆ ](#a08dae9b6fbda60f06430cb2b842280b9)address

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xfer\_packet::address |
| --- |

Transfer Address.

## [◆ ](#aedc8eadfb3a0737c3984b130ec21d96c)cb\_mask

| enum [mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) mspi\_xfer\_packet::cb\_mask |
| --- |

Bus event callback masks.

## [◆ ](#a2717e86b7fbb01be65a4955a8e26ebc0)cmd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xfer\_packet::cmd |
| --- |

Transfer command.

## [◆ ](#a0b7b3d68ff46173378e4076b439e35ac)data\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* mspi\_xfer\_packet::data\_buf |
| --- |

Data Buffer.

## [◆ ](#afb408ea48ff8863c9714d39c4f7c8a2c)dir

| enum [mspi\_xfer\_direction](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6) mspi\_xfer\_packet::dir |
| --- |

Direction (Transmit/Receive).

## [◆ ](#a050a827d0ee0349cd7a006de20b1db0c)num\_bytes

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xfer\_packet::num\_bytes |
| --- |

Number of bytes to transfer.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_xfer\_packet](structmspi__xfer__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
