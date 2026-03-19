---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usb__bos.html
original_path: doxygen/html/group__usb__bos.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB BOS support

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USB Binary Device Object Store support.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usb\_bos\_descriptor](structusb__bos__descriptor.md) |
|  | Root BOS Descriptor. [More...](structusb__bos__descriptor.md#details) |
| struct | [usb\_bos\_capability\_lpm](structusb__bos__capability__lpm.md) |
|  | BOS USB 2.0 extension capability descriptor. [More...](structusb__bos__capability__lpm.md#details) |
| struct | [usb\_bos\_platform\_descriptor](structusb__bos__platform__descriptor.md) |
|  | BOS platform capability descriptor. [More...](structusb__bos__platform__descriptor.md#details) |
| struct | [usb\_bos\_capability\_webusb](structusb__bos__capability__webusb.md) |
|  | WebUSB specific part of platform capability descriptor. [More...](structusb__bos__capability__webusb.md#details) |
| struct | [usb\_bos\_capability\_msos](structusb__bos__capability__msos.md) |
|  | Microsoft OS 2.0 descriptor specific part of platform capability descriptor. [More...](structusb__bos__capability__msos.md#details) |

| Enumerations | |
| --- | --- |
| enum | [usb\_bos\_capability\_types](#ga0bddefd6b9373068cd4ff8e6fc47950d) { [USB\_BOS\_CAPABILITY\_EXTENSION](#gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862) = 0x02 , [USB\_BOS\_CAPABILITY\_PLATFORM](#gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b) = 0x05 } |
|  | Device capability type codes. [More...](#ga0bddefd6b9373068cd4ff8e6fc47950d) |

## Detailed Description

USB Binary Device Object Store support.

Since
:   1.13

Version
:   1.0.0

## Enumeration Type Documentation

## [◆ ](#ga0bddefd6b9373068cd4ff8e6fc47950d)usb\_bos\_capability\_types

| enum [usb\_bos\_capability\_types](#ga0bddefd6b9373068cd4ff8e6fc47950d) |
| --- |

`#include <[bos.h](bos_8h.md)>`

Device capability type codes.

| Enumerator | |
| --- | --- |
| USB\_BOS\_CAPABILITY\_EXTENSION |  |
| USB\_BOS\_CAPABILITY\_PLATFORM |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
