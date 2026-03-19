---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structled__info.html
original_path: doxygen/html/structled__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led\_info Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [LED Interface](group__led__interface.md)

LED information structure.
[More...](#details)

`#include <[led.h](drivers_2led_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [label](#a5d01795e49663654e9fe4a821797956a) |
|  | LED label. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [index](#a7f87ebb0718e1dc189e6d48d5bb97c55) |
|  | Index of the LED on the controller. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_colors](#ab6db05157b960669e3b01154a9621530) |
|  | Number of colors per LED. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [color\_mapping](#a8daacbe0a68d7ff710938722003fceaf) |
|  | Mapping of the LED colors. |

## Detailed Description

LED information structure.

This structure gathers useful information about LED controller.

## Field Documentation

## [◆ ](#a8daacbe0a68d7ff710938722003fceaf)color\_mapping

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* led\_info::color\_mapping |
| --- |

Mapping of the LED colors.

## [◆ ](#a7f87ebb0718e1dc189e6d48d5bb97c55)index

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led\_info::index |
| --- |

Index of the LED on the controller.

## [◆ ](#a5d01795e49663654e9fe4a821797956a)label

| const char\* led\_info::label |
| --- |

LED label.

## [◆ ](#ab6db05157b960669e3b01154a9621530)num\_colors

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) led\_info::num\_colors |
| --- |

Number of colors per LED.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[led.h](drivers_2led_8h_source.md)

- [led\_info](structled__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
