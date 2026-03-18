---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpd__msg.html
original_path: doxygen/html/structpd__msg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_msg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Power Delivery message.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [pd\_packet\_type](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b) | [type](#af9f676afd2c2824fb9f01a08d8339231) |
|  | Type of this packet. |
| union [pd\_header](unionpd__header.md) | [header](#ae6f1fa8a1fb006e3d90e75cd834e6d05) |
|  | Header of this message. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#aa03ec4ce6d2f0d16a829394ff0ed2688) |
|  | Length of bytes in data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#ad6fd282617b5f6dfeeef6cf4598883ee) [260] |
|  | Message data. |

## Detailed Description

Power Delivery message.

## Field Documentation

## [◆ ](#ad6fd282617b5f6dfeeef6cf4598883ee)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pd\_msg::data[260] |
| --- |

Message data.

## [◆ ](#ae6f1fa8a1fb006e3d90e75cd834e6d05)header

| union [pd\_header](unionpd__header.md) pd\_msg::header |
| --- |

Header of this message.

## [◆ ](#aa03ec4ce6d2f0d16a829394ff0ed2688)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_msg::len |
| --- |

Length of bytes in data.

## [◆ ](#af9f676afd2c2824fb9f01a08d8339231)type

| enum [pd\_packet\_type](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b) pd\_msg::type |
| --- |

Type of this packet.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_msg](structpd__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
