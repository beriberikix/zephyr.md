---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtcpci__reg__dump__map.html
original_path: doxygen/html/structtcpci__reg__dump__map.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpci\_reg\_dump\_map Struct Reference

Structure used to bind the register address to name in registers dump.
[More...](#details)

`#include <[tcpci_priv.h](tcpci__priv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#ad68dd201d76bfb2193567b8db2ec514a) |
|  | Address of I2C device register. |
| const char \* | [name](#a316d7f2a6b4b5fd42eb6450a810b7dd8) |
|  | Human readable name of register. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [size](#a6e84093c1d027233230d8f27b0698756) |
|  | Size in bytes of the register. |

## Detailed Description

Structure used to bind the register address to name in registers dump.

## Field Documentation

## [◆ ](#ad68dd201d76bfb2193567b8db2ec514a)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcpci\_reg\_dump\_map::addr |
| --- |

Address of I2C device register.

## [◆ ](#a316d7f2a6b4b5fd42eb6450a810b7dd8)name

| const char\* tcpci\_reg\_dump\_map::name |
| --- |

Human readable name of register.

## [◆ ](#a6e84093c1d027233230d8f27b0698756)size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcpci\_reg\_dump\_map::size |
| --- |

Size in bytes of the register.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[tcpci\_priv.h](tcpci__priv_8h_source.md)

- [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
