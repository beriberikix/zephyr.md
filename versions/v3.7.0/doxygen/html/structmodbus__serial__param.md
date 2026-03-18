---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodbus__serial__param.html
original_path: doxygen/html/structmodbus__serial__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus\_serial\_param Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MODBUS](group__modbus.md)

Modbus serial line parameter.
[More...](#details)

`#include <[modbus.h](modbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [baud](#af3989f5e20eb96080d456114ef4d86e5) |
|  | Baudrate of the serial line. |
| enum [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) | [parity](#a337a18f3ad923bf758cb432b9a2d8ada) |
|  | parity UART's parity setting: UART\_CFG\_PARITY\_NONE, UART\_CFG\_PARITY\_EVEN, UART\_CFG\_PARITY\_ODD |
| enum [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) | [stop\_bits\_client](#a6f5819e3fbaf756f9150fdff431196c4) |
|  | stop\_bits\_client UART's stop bits setting if in client mode: UART\_CFG\_STOP\_BITS\_0\_5, UART\_CFG\_STOP\_BITS\_1, UART\_CFG\_STOP\_BITS\_1\_5, UART\_CFG\_STOP\_BITS\_2, |

## Detailed Description

Modbus serial line parameter.

## Field Documentation

## [◆ ](#af3989f5e20eb96080d456114ef4d86e5)baud

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modbus\_serial\_param::baud |
| --- |

Baudrate of the serial line.

## [◆ ](#a337a18f3ad923bf758cb432b9a2d8ada)parity

| enum [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) modbus\_serial\_param::parity |
| --- |

parity UART's parity setting: UART\_CFG\_PARITY\_NONE, UART\_CFG\_PARITY\_EVEN, UART\_CFG\_PARITY\_ODD

## [◆ ](#a6f5819e3fbaf756f9150fdff431196c4)stop\_bits\_client

| enum [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) modbus\_serial\_param::stop\_bits\_client |
| --- |

stop\_bits\_client UART's stop bits setting if in client mode: UART\_CFG\_STOP\_BITS\_0\_5, UART\_CFG\_STOP\_BITS\_1, UART\_CFG\_STOP\_BITS\_1\_5, UART\_CFG\_STOP\_BITS\_2,

---

The documentation for this struct was generated from the following file:

- zephyr/modbus/[modbus.h](modbus_8h_source.md)

- [modbus\_serial\_param](structmodbus__serial__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
