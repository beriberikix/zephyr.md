---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structuart__config.html
original_path: doxygen/html/structuart__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md)

UART controller configuration structure.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [baudrate](#ab532159a689e8f38c2465ce2d1fef354) |
|  | Baudrate setting in bps. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [parity](#a9371728729252797880de052aae01089) |
|  | Parity bit, use [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711 "uart_config_parity"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [stop\_bits](#a7b98cd63c531110dc3dc99e94db73642) |
|  | Stop bits, use [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e "uart_config_stop_bits"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_bits](#a93ee24cf6669fb4cfece78a53d3ec6c5) |
|  | Data bits, use [uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a "uart_config_data_bits"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flow\_ctrl](#af259c5efab532920b5cce7ae57f6af5e) |
|  | Flow control setting, use [uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8 "uart_config_flow_control"). |

## Detailed Description

UART controller configuration structure.

## Field Documentation

## [◆ ](#ab532159a689e8f38c2465ce2d1fef354)baudrate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uart\_config::baudrate |
| --- |

Baudrate setting in bps.

## [◆ ](#a93ee24cf6669fb4cfece78a53d3ec6c5)data\_bits

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_config::data\_bits |
| --- |

Data bits, use [uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a "uart_config_data_bits").

## [◆ ](#af259c5efab532920b5cce7ae57f6af5e)flow\_ctrl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_config::flow\_ctrl |
| --- |

Flow control setting, use [uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8 "uart_config_flow_control").

## [◆ ](#a9371728729252797880de052aae01089)parity

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_config::parity |
| --- |

Parity bit, use [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711 "uart_config_parity").

## [◆ ](#a7b98cd63c531110dc3dc99e94db73642)stop\_bits

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_config::stop\_bits |
| --- |

Stop bits, use [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e "uart_config_stop_bits").

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_config](structuart__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
