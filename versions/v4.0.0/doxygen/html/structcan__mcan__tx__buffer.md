---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__mcan__tx__buffer.html
original_path: doxygen/html/structcan__mcan__tx__buffer.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_tx\_buffer Struct Reference

Bosch M\_CAN Tx Buffer Element.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md) | [hdr](#a5b553813e69bf22565d2894e8137672d) |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [data](#af69274236867987f069aa6dd29182f82) [64] |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [data\_32](#a4b1a8963e8da21c01843f20e9e01bb11) [16] |  |
| }; |  |

## Detailed Description

Bosch M\_CAN Tx Buffer Element.

See Bosch M\_CAN Users Manual section 2.4.3 for details.

## Field Documentation

## [◆ ](#ac8b322cfb94b89abb453307d502a99d9)[union]

| union { ... } [can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md) |
| --- |

## [◆ ](#af69274236867987f069aa6dd29182f82)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer::data[64] |
| --- |

## [◆ ](#a4b1a8963e8da21c01843f20e9e01bb11)data\_32

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer::data\_32[16] |
| --- |

## [◆ ](#a5b553813e69bf22565d2894e8137672d)hdr

| struct [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md) can\_mcan\_tx\_buffer::hdr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
