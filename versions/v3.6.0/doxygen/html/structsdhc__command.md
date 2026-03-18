---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsdhc__command.html
original_path: doxygen/html/structsdhc__command.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc\_command Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SDHC interface](group__sdhc__interface.md)

SD host controller command structure.
[More...](#details)

`#include <[sdhc.h](sdhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [opcode](#a320ad415df67e1d9b4c09f95993dd17f) |
|  | SD Host specification CMD index. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arg](#af6b98d5f1cecf25af2480b1d359f200e) |
|  | SD host specification argument. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [response](#a37a3c1608b5c13311c833c4ad24ff1f9) [4] |
|  | SD card response field. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [response\_type](#af758a4e0e3b090912f6e9abd7c4be8f3) |
|  | Expected SD response type. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [retries](#a39ba0b1e99814471939dc7bbb7d098eb) |
|  | Max number of retries. |
| int | [timeout\_ms](#a92cf023d28aa6106d603ff7f67a7e04b) |
|  | Command timeout in milliseconds. |

## Detailed Description

SD host controller command structure.

This command structure is used to send command requests to an SD host controller, which will be sent to SD devices.

## Field Documentation

## [◆ ](#af6b98d5f1cecf25af2480b1d359f200e)arg

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_command::arg |
| --- |

SD host specification argument.

## [◆ ](#a320ad415df67e1d9b4c09f95993dd17f)opcode

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_command::opcode |
| --- |

SD Host specification CMD index.

## [◆ ](#a37a3c1608b5c13311c833c4ad24ff1f9)response

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_command::response[4] |
| --- |

SD card response field.

## [◆ ](#af758a4e0e3b090912f6e9abd7c4be8f3)response\_type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_command::response\_type |
| --- |

Expected SD response type.

## [◆ ](#a39ba0b1e99814471939dc7bbb7d098eb)retries

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_command::retries |
| --- |

Max number of retries.

## [◆ ](#a92cf023d28aa6106d603ff7f67a7e04b)timeout\_ms

| int sdhc\_command::timeout\_ms |
| --- |

Command timeout in milliseconds.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sdhc.h](sdhc_8h_source.md)

- [sdhc\_command](structsdhc__command.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
